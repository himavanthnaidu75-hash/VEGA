import pandas as pd
from typing import List, Optional
from .base import BrokerInterface, Position, FundSummary, OrderResult
from dhanhq import dhanhq
from ..core.config import settings
from loguru import logger

class DhanBroker(BrokerInterface):
    def __init__(self):
        self.dhan = dhanhq(settings.DHAN_CLIENT_ID, settings.DHAN_ACCESS_TOKEN)

    def connect(self) -> bool:
        try:
            self.dhan.get_fund_limits()
            return True
        except Exception as e:
            logger.error(f"Dhan Connection Failed: {e}")
            return False

    def get_positions(self) -> List[Position]:
        resp = self.dhan.get_positions()
        positions = []
        if resp.get('status') == 'success':
            for pos in resp.get('data', []):
                positions.append(Position(
                    symbol=pos['tradingSymbol'],
                    qty=int(pos['netQty']),
                    entry_price=float(pos['avgPrice']),
                    current_price=float(pos['lastTradedPrice']),
                    pnl=float(pos['unrealizedProfit'])
                ))
        return positions

    def get_orders(self) -> List[dict]:
        resp = self.dhan.get_order_list()
        return resp.get('data', []) if resp.get('status') == 'success' else []

    def get_funds(self) -> FundSummary:
        resp = self.dhan.get_fund_limits()
        if resp.get('status') == 'success':
            data = resp['data']
            return FundSummary(
                available_margin=float(data.get('availabelBalance', 0)),
                utilized_margin=float(data.get('utilizedAmount', 0))
            )
        return FundSummary(available_margin=0.0, utilized_margin=0.0)

    def place_order(self, symbol: str, qty: int, side: str, order_type: str, price: float = 0.0, product: str = "MIS") -> OrderResult:
        resp = self.dhan.place_order(
            tag='vega',
            transaction_type=side.upper(),
            exchange='NSE',
            symbol=symbol,
            quantity=qty,
            order_type=order_type.upper(),
            product_type=product.upper(),
            price=price
        )
        if resp.get('status') == 'success':
            return OrderResult(order_id=resp['data']['orderId'], status='SUCCESS')
        return OrderResult(order_id='', status='FAILED', message=resp.get('remarks'))

    def cancel_order(self, order_id: str) -> bool:
        resp = self.dhan.cancel_order(order_id)
        return resp.get('status') == 'success'

    def cancel_all_orders(self) -> bool:
        orders = self.get_orders()
        success = True
        for order in orders:
            if order.get('orderStatus') in ['PENDING', 'TRANSIT']:
                if not self.cancel_order(order['orderId']):
                    success = False
        return success

    def modify_order(self, order_id: str, price: float, qty: int) -> bool:
        resp = self.dhan.modify_order(order_id, price=price, quantity=qty)
        return resp.get('status') == 'success'

    def get_live_price(self, symbol: str) -> float:
        return 0.0 # Placeholder for Dhan ticker logic

    def get_ohlcv(self, symbol: str, interval: str, from_date: str, to_date: str) -> pd.DataFrame:
        return pd.DataFrame()

    def subscribe_live_feed(self, symbols: List[str], callback: callable) -> None:
        pass
