import pandas as pd
from typing import List, Optional
from .base import BrokerInterface, Position, FundSummary, OrderResult
from kiteconnect import KiteConnect
from ..core.config import settings
from loguru import logger

class ZerodhaBroker(BrokerInterface):
    def __init__(self):
        logger.warning("!!! ZERODHA IS A PAID API BROKER (₹2000/MONTH) !!!")
        self.kite = KiteConnect(api_key=settings.ZERODHA_API_KEY)
        self.kite.set_access_token(settings.ZERODHA_ACCESS_TOKEN)

    def connect(self) -> bool:
        try:
            self.kite.margins()
            return True
        except Exception as e:
            logger.error(f"Zerodha Connection Failed: {e}")
            return False

    def get_positions(self) -> List[Position]:
        resp = self.kite.positions()
        positions = []
        for pos in resp.get('net', []):
            positions.append(Position(
                symbol=pos['tradingsymbol'],
                qty=int(pos['quantity']),
                entry_price=float(pos['average_price']),
                current_price=float(pos['last_price']),
                pnl=float(pos['pnl'])
            ))
        return positions

    def get_orders(self) -> List[dict]:
        return self.kite.orders()

    def get_funds(self) -> FundSummary:
        margins = self.kite.margins()
        equity = margins.get('equity', {})
        return FundSummary(
            available_margin=float(equity.get('available', {}).get('cash', 0)),
            utilized_margin=float(equity.get('utilised', {}).get('debits', 0))
        )

    def place_order(self, symbol: str, qty: int, side: str, order_type: str, price: float = 0.0, product: str = "MIS") -> OrderResult:
        try:
            order_id = self.kite.place_order(
                variety=self.kite.VARIETY_REGULAR,
                exchange=self.kite.EXCHANGE_NSE,
                tradingsymbol=symbol,
                transaction_type=side.upper(),
                quantity=qty,
                product=product.upper(),
                order_type=order_type.upper(),
                price=price
            )
            return OrderResult(order_id=order_id, status='SUCCESS')
        except Exception as e:
            return OrderResult(order_id='', status='FAILED', message=str(e))

    def cancel_order(self, order_id: str) -> bool:
        try:
            self.kite.cancel_order(self.kite.VARIETY_REGULAR, order_id)
            return True
        except: return False

    def cancel_all_orders(self) -> bool:
        orders = self.get_orders()
        for o in orders:
            if o['status'] in ['OPEN', 'PENDING']:
                self.cancel_order(o['order_id'])
        return True

    def modify_order(self, order_id: str, price: float, qty: int) -> bool:
        return False

    def get_live_price(self, symbol: str) -> float:
        return 0.0

    def get_ohlcv(self, symbol: str, interval: str, from_date: str, to_date: str) -> pd.DataFrame:
        return pd.DataFrame()

    def subscribe_live_feed(self, symbols: List[str], callback: callable) -> None:
        pass
