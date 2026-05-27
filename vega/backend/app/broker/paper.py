import pandas as pd
import yfinance as yf
from typing import List, Dict, Optional
from .base import BrokerInterface, Position, FundSummary, OrderResult
from pydantic import BaseModel
import uuid
import datetime

class PaperOrder(BaseModel):
    order_id: str
    symbol: str
    qty: int
    side: str
    order_type: str
    price: float
    status: str
    timestamp: datetime.datetime

class PaperBroker(BrokerInterface):
    def __init__(self, initial_capital: float = 100000.0):
        self.capital = initial_capital
        self.positions: Dict[str, Position] = {}
        self.orders: List[PaperOrder] = []
        self.margins = FundSummary(available_margin=initial_capital, utilized_margin=0.0)

    def connect(self) -> bool: return True
    def get_positions(self) -> List[Position]:
        for symbol, pos in self.positions.items():
            current_price = self.get_live_price(symbol)
            pos.current_price = current_price
            pos.pnl = (current_price - pos.entry_price) * pos.qty if pos.qty > 0 else (pos.entry_price - current_price) * abs(pos.qty)
        return list(self.positions.values())
    def get_orders(self) -> List[dict]: return [order.dict() for order in self.orders]
    def get_funds(self) -> FundSummary: return self.margins
    def place_order(self, symbol: str, qty: int, side: str, order_type: str, price: float = 0.0, product: str = "MIS") -> OrderResult:
        current_price = self.get_live_price(symbol)
        exec_price = price if order_type == "LIMIT" else current_price
        order_id = str(uuid.uuid4())
        order = PaperOrder(order_id=order_id, symbol=symbol, qty=qty, side=side, order_type=order_type, price=exec_price, status="FILLED", timestamp=datetime.datetime.now())
        self.orders.append(order)
        if side.upper() == "BUY":
            if symbol in self.positions:
                pos = self.positions[symbol]
                new_qty = pos.qty + qty
                pos.entry_price = (pos.entry_price * pos.qty + exec_price * qty) / new_qty
                pos.qty = new_qty
            else:
                self.positions[symbol] = Position(symbol=symbol, qty=qty, entry_price=exec_price, current_price=exec_price, pnl=0.0)
            self.margins.utilized_margin += exec_price * qty
            self.margins.available_margin -= exec_price * qty
        else:
            if symbol in self.positions:
                pos = self.positions[symbol]
                new_qty = pos.qty - qty
                if new_qty == 0: del self.positions[symbol]
                else: pos.qty = new_qty
                self.margins.utilized_margin -= exec_price * qty
                self.margins.available_margin += exec_price * qty
            else:
                self.positions[symbol] = Position(symbol=symbol, qty=-qty, entry_price=exec_price, current_price=exec_price, pnl=0.0)
                self.margins.utilized_margin += exec_price * qty
                self.margins.available_margin -= exec_price * qty
        return OrderResult(order_id=order_id, status="FILLED")
    def cancel_order(self, order_id: str) -> bool: return True
    def cancel_all_orders(self) -> bool: return True
    def modify_order(self, order_id: str, price: float, qty: int) -> bool: return False
    def get_live_price(self, symbol: str) -> float:
        yf_symbol = f"{symbol}.NS" if not symbol.endswith((".NS", ".BO")) else symbol
        try:
            ticker = yf.Ticker(yf_symbol)
            data = ticker.history(period="1d")
            return data['Close'].iloc[-1] if not data.empty else 0.0
        except: return 0.0
    def get_ohlcv(self, symbol: str, interval: str, from_date: str, to_date: str) -> pd.DataFrame:
        yf_symbol = f"{symbol}.NS" if not symbol.endswith((".NS", ".BO")) else symbol
        return yf.download(yf_symbol, start=from_date, end=to_date, interval=interval)
    def subscribe_live_feed(self, symbols: List[str], callback: callable) -> None: pass
