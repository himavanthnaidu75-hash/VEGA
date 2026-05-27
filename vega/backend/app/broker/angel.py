import pandas as pd
from typing import List, Optional
from .base import BrokerInterface, Position, FundSummary, OrderResult
from SmartApi import SmartConnect
from ..core.config import settings
from loguru import logger

class AngelOneBroker(BrokerInterface):
    def __init__(self):
        self.smart_api = SmartConnect(api_key=settings.ANGEL_API_KEY)
        self.session_data = None

    def connect(self) -> bool:
        try:
            self.session_data = self.smart_api.generateSession(settings.ANGEL_CLIENT_ID, settings.ANGEL_PASSWORD, settings.ANGEL_TOTP_SECRET)
            return True
        except Exception as e:
            logger.error(f"AngelOne Connection Failed: {e}")
            return False

    def get_positions(self) -> List[Position]:
        resp = self.smart_api.position()
        positions = []
        if resp.get('status'):
            for pos in resp.get('data', []):
                positions.append(Position(
                    symbol=pos['tradingsymbol'],
                    qty=int(pos['netqty']),
                    entry_price=float(pos['avgprice']),
                    current_price=float(pos['ltp']),
                    pnl=float(pos['pnl'])
                ))
        return positions

    def get_orders(self) -> List[dict]:
        resp = self.smart_api.orderBook()
        return resp.get('data', []) if resp.get('status') else []

    def get_funds(self) -> FundSummary:
        resp = self.smart_api.rmsLimit()
        if resp.get('status'):
            data = resp['data']
            return FundSummary(
                available_margin=float(data.get('net', 0)),
                utilized_margin=0.0 # Angel uses complex limit structure
            )
        return FundSummary(available_margin=0.0, utilized_margin=0.0)

    def place_order(self, symbol: str, qty: int, side: str, order_type: str, price: float = 0.0, product: str = "MIS") -> OrderResult:
        # Simplified AngelOne order placement
        params = {
            "variety": "NORMAL",
            "tradingsymbol": symbol,
            "symboltoken": "12345", # Mapping needed
            "transactiontype": side.upper(),
            "exchange": "NSE",
            "ordertype": order_type.upper(),
            "producttype": product.upper(),
            "duration": "DAY",
            "price": str(price),
            "quantity": str(qty)
        }
        resp = self.smart_api.placeOrder(params)
        if resp.get('status'):
            return OrderResult(order_id=resp['data']['orderid'], status='SUCCESS')
        return OrderResult(order_id='', status='FAILED', message=resp.get('message'))

    def cancel_order(self, order_id: str) -> bool:
        resp = self.smart_api.cancelOrder("NORMAL", order_id)
        return resp.get('status') == True

    def cancel_all_orders(self) -> bool:
        orders = self.get_orders()
        for o in orders:
            if o['status'] in ['open', 'pending']:
                self.cancel_order(o['orderid'])
        return True

    def modify_order(self, order_id: str, price: float, qty: int) -> bool:
        return False

    def get_live_price(self, symbol: str) -> float:
        return 0.0

    def get_ohlcv(self, symbol: str, interval: str, from_date: str, to_date: str) -> pd.DataFrame:
        return pd.DataFrame()

    def subscribe_live_feed(self, symbols: List[str], callback: callable) -> None:
        pass
