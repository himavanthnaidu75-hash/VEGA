import requests
from .base import BrokerAdapter

class DhanAdapter(BrokerAdapter):
    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token
        self.base_url = "https://api.dhan.co"
        self.headers = {
            "access-token": self.access_token,
            "client-id": self.client_id,
            "Content-Type": "application/json"
        }

    def get_balance(self):
        url = f"{self.base_url}/fundlimit"
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def place_order(self, symbol, side, qty, order_type, price=None):
        # Implementation depends on Dhan's exact payload structure
        # This is a skeleton based on general Dhan API patterns
        url = f"{self.base_url}/orders"
        payload = {
            "dhanClientId": self.client_id,
            "transactionType": side,
            "exchangeSegment": "NSE_EQ",
            "productType": "INTRADAY",
            "orderType": "MARKET" if not price else "LIMIT",
            "validity": "DAY",
            "tradingSymbol": symbol,
            "securityId": "1234", # Should be mapped from symbol
            "quantity": qty,
            "price": price or 0
        }
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def get_positions(self):
        url = f"{self.base_url}/positions"
        try:
            response = requests.get(url, headers=self.headers)
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def stream_quotes(self, symbols):
        # Dhan uses a separate Market Data API for WebSocket
        # Implementation would involve a WebSocket client
        pass
