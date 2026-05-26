import asyncio
from datetime import datetime
from .strategy_engine import StrategyEngine
from .risk_manager import RiskManager
from ..services.data_service import DataService
from ..adapters.factory import get_broker_adapter

class VegaOrchestrator:
    def __init__(self, symbols=["RELIANCE.NS", "TCS.NS", "INFY.NS"]):
        self.symbols = symbols
        self.data_service = DataService()
        self.strategy_engine = StrategyEngine(self.data_service)
        self.broker = get_broker_adapter("PAPER")
        self.risk_manager = RiskManager(total_capital=100000)
        self.is_running = False
        self.active_trades = []

    async def start(self):
        self.is_running = True
        print("VEGA Orchestrator Started")
        while self.is_running:
            now = datetime.now()
            # 3:15 PM IST Auto Square-off
            if now.hour == 15 and now.minute >= 15:
                await self.square_off_all()
                break

            for symbol in self.symbols:
                await self.process_symbol(symbol)

            await asyncio.sleep(60) # Scan every minute

    async def process_symbol(self, symbol):
        # 1. Fetch Data
        htf_df = self.data_service.get_historical_data(symbol, period="2d", interval="15m")
        ltf_df = self.data_service.get_historical_data(symbol, period="1d", interval="1m")

        if htf_df.empty or ltf_df.empty: return

        # 2. Get Major Levels (PDH/PDL)
        pd_high = htf_df['High'].iloc[-2] # Previous day high approx
        pd_low = htf_df['Low'].iloc[-2]
        major_levels = [pd_high, pd_low]

        # 3. Generate Signals
        signals = self.strategy_engine.generate_signals(symbol, htf_df, ltf_df, major_levels)

        for sig in signals:
            await self.execute_trade(sig)

    async def execute_trade(self, signal):
        # Calculate SL/TP
        entry = signal['price']
        if signal['side'] == 'BUY':
            sl = entry * 0.99
            tp = entry * 1.02
        else:
            sl = entry * 1.01
            tp = entry * 0.98

        if self.risk_manager.validate_trade(entry, sl, tp):
            qty = self.risk_manager.calculate_position_size(entry, sl)
            if qty > 0:
                print(f"Executing {signal['side']} for {signal['symbol']} @ {entry} (Qty: {qty})")
                order = self.broker.place_order(signal['symbol'], signal['side'], qty, "MARKET")
                self.active_trades.append(order)

    async def square_off_all(self):
        print("Market closing. Squaring off all positions.")
        # Logic to close positions via broker
        self.active_trades = []
        self.is_running = False

    def stop(self):
        self.is_running = False
