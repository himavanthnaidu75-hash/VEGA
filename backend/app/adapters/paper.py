from .base import BrokerAdapter
import uuid

class PaperAdapter(BrokerAdapter):
    def __init__(self, balance=100000):
        self.balance = balance
        self.positions = {}
        self.orders = []

    def get_balance(self):
        return {"balance": self.balance, "currency": "INR"}

    def place_order(self, symbol, side, qty, order_type, price=None):
        order_id = str(uuid.uuid4())
        order = {
            "order_id": order_id,
            "symbol": symbol,
            "side": side,
            "qty": qty,
            "type": order_type,
            "status": "FILLED",
            "price": price
        }
        self.orders.append(order)
        # Update paper positions
        if side == "BUY":
            self.positions[symbol] = self.positions.get(symbol, 0) + qty
        else:
            self.positions[symbol] = self.positions.get(symbol, 0) - qty

        return order

    def get_positions(self):
        return self.positions

    def stream_quotes(self, symbols):
        # Simulated stream
        return {s: 0.0 for s in symbols}
