import asyncio
from typing import List, Dict
from loguru import logger
from ..broker.factory import get_broker
from ..engine.strategy_engine import StrategyEngine
from ..engine.risk_manager import RiskManager
from ..engine.ict_engine import ICTConfirmationModel
from ..services.data_service import DataService
from ..core.config import settings
from ..models.trade import Trade
from ..core.database import engine
from sqlmodel import Session, select
import datetime
import pytz

class TradingOrchestrator:
    def __init__(self):
        self.broker = get_broker()
        self.strategy_engine = StrategyEngine()
        self.risk_manager = RiskManager(settings.TOTAL_CAPITAL)
        self.ict_model = ICTConfirmationModel()
        self.is_running = False
        self.current_session = None

    async def start_scanning(self):
        self.is_running = True
        logger.info("Trading Orchestrator started scanning...")
        while self.is_running:
            try:
                await self.run_scan_cycle()
            except Exception as e:
                logger.error(f"Error in scan cycle: {e}")
            await asyncio.sleep(60) # Scan every 60 seconds

    async def run_scan_cycle(self):
        watchlist = settings.WATCHLIST.split(",")
        data_5m = {}
        data_15m = {}

        # 1. Fetch Data
        for symbol in watchlist:
            df_5m = DataService.fetch_ohlcv(symbol, interval="5m", period="5d")
            df_15m = DataService.fetch_ohlcv(symbol, interval="15m", period="10d")
            if not df_5m.empty:
                data_5m[symbol] = df_5m
                data_15m[symbol] = df_15m

        # 2. Run Strategies
        signals = self.strategy_engine.run_all(data_5m)

        # 3. Process Signals
        for signal in signals:
            await self.process_signal(signal, data_5m[signal['symbol']], data_15m[signal['symbol']])

    async def process_signal(self, signal: Dict, df_5m, df_15m):
        symbol = signal['symbol']

        # 1. ICT Confirmation
        ict_score = self.ict_model.calculate_confidence(df_5m, df_15m)
        total_score = ict_score + signal.get('confidence_boost', 0)

        if total_score < settings.ICT_MIN_CONFIDENCE:
            logger.info(f"Signal rejected: {symbol} {signal['strategy']} Score {total_score} < {settings.ICT_MIN_CONFIDENCE}")
            return

        # 2. Risk Management
        with Session(engine) as session:
            open_trades = session.exec(select(Trade).where(Trade.status == "OPEN")).all()
            if not self.risk_manager.validate_trade(signal['entry'], signal['sl'], signal['tp'], len(open_trades)):
                logger.info(f"Signal rejected by Risk Manager: {symbol}")
                return

            qty = self.risk_manager.calculate_position_size(signal['entry'], signal['sl'])
            if qty <= 0: return

            # 3. Place Order
            logger.info(f"Placing {signal['side']} order for {symbol} Qty: {qty} Strategy: {signal['strategy']} Score: {total_score}")
            order_res = self.broker.place_order(
                symbol=symbol,
                qty=qty,
                side=signal['side'],
                order_type="MARKET"
            )

            if order_res.status == "FILLED" or order_res.status == "SUCCESS":
                trade = Trade(
                    symbol=symbol,
                    strategy=signal['strategy'],
                    ict_score=total_score,
                    side=signal['side'],
                    qty=qty,
                    entry_price=signal['entry'],
                    sl=signal['sl'],
                    tp=signal['tp'],
                    order_id=order_res.order_id
                )
                session.add(trade)
                session.commit()
                logger.success(f"Trade executed: {symbol} @ {signal['entry']}")

    async def square_off_all(self):
        logger.warning("Squaring off all positions...")
        positions = self.broker.get_positions()
        for pos in positions:
            if pos.qty != 0:
                side = "SELL" if pos.qty > 0 else "BUY"
                self.broker.place_order(pos.symbol, abs(pos.qty), side, "MARKET")

        with Session(engine) as session:
            open_trades = session.exec(select(Trade).where(Trade.status == "OPEN")).all()
            for trade in open_trades:
                trade.status = "CLOSED"
                trade.exit_time = datetime.datetime.utcnow()
                session.add(trade)
            session.commit()
