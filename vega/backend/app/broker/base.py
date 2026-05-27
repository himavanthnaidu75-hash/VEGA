from abc import ABC, abstractmethod
from typing import List, Optional
import pandas as pd
from pydantic import BaseModel

class OrderResult(BaseModel):
    order_id: str
    status: str
    message: Optional[str] = None

class Position(BaseModel):
    symbol: str
    qty: int
    entry_price: float
    current_price: float
    pnl: float

class FundSummary(BaseModel):
    available_margin: float
    utilized_margin: float

class BrokerInterface(ABC):
    @abstractmethod
    def connect(self) -> bool: pass
    @abstractmethod
    def get_positions(self) -> List[Position]: pass
    @abstractmethod
    def get_orders(self) -> List[dict]: pass
    @abstractmethod
    def get_funds(self) -> FundSummary: pass
    @abstractmethod
    def place_order(self, symbol: str, qty: int, side: str, order_type: str, price: float = 0.0, product: str = "MIS") -> OrderResult: pass
    @abstractmethod
    def cancel_order(self, order_id: str) -> bool: pass
    @abstractmethod
    def cancel_all_orders(self) -> bool: pass
    @abstractmethod
    def modify_order(self, order_id: str, price: float, qty: int) -> bool: pass
    @abstractmethod
    def get_live_price(self, symbol: str) -> float: pass
    @abstractmethod
    def get_ohlcv(self, symbol: str, interval: str, from_date: str, to_date: str) -> pd.DataFrame: pass
    @abstractmethod
    def subscribe_live_feed(self, symbols: List[str], callback: callable) -> None: pass
