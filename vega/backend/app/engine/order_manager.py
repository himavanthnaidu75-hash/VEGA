import asyncio
from typing import List, Dict
from loguru import logger
from ..adapters.base import BrokerInterface, OrderResult
from ..models.trade import Trade
from ..core.database import engine
from sqlmodel import Session, select
import datetime

class OrderManager:
    def __init__(self, broker: BrokerInterface):
        self.broker = broker

    async def update_open_trades(self):
        """Updates stop loss and target profit for open trades."""
        with Session(engine) as session:
            trades = session.exec(select(Trade).where(Trade.status == "OPEN")).all()
            for trade in trades:
                try:
                    current_price = self.broker.get_live_price(trade.symbol)
                    if current_price == 0: continue

                    # 1. Check Exit Conditions
                    if trade.side == "BUY":
                        if current_price <= trade.sl:
                            logger.info(f"SL Hit for {trade.symbol} @ {current_price}")
                            await self.close_trade(trade, current_price, "SL HIT")
                        elif current_price >= trade.tp:
                            logger.info(f"TP Hit for {trade.symbol} @ {current_price}")
                            await self.close_trade(trade, current_price, "TP HIT")
                    else: # SELL
                        if current_price >= trade.sl:
                            logger.info(f"SL Hit for {trade.symbol} @ {current_price}")
                            await self.close_trade(trade, current_price, "SL HIT")
                        elif current_price <= trade.tp:
                            logger.info(f"TP Hit for {trade.symbol} @ {current_price}")
                            await self.close_trade(trade, current_price, "TP HIT")

                    # 2. Trailing Stop Loss Logic (if enabled)
                    # Implementation detail...

                except Exception as e:
                    logger.error(f"Error updating trade {trade.id}: {e}")

    async def close_trade(self, trade: Trade, exit_price: float, reason: str):
        side = "SELL" if trade.side == "BUY" else "BUY"
        res = self.broker.place_order(trade.symbol, trade.qty, side, "MARKET")

        with Session(engine) as session:
            # Refresh trade object
            db_trade = session.get(Trade, trade.id)
            db_trade.status = "CLOSED"
            db_trade.exit_price = exit_price
            db_trade.exit_time = datetime.datetime.utcnow()
            db_trade.pnl = (exit_price - trade.entry_price) * trade.qty if trade.side == "BUY" else (trade.entry_price - exit_price) * trade.qty
            session.add(db_trade)
            session.commit()
            logger.success(f"Closed {trade.symbol} Reason: {reason} PnL: {db_trade.pnl}")
