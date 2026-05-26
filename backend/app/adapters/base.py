from abc import ABC, abstractmethod

class BrokerAdapter(ABC):
    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def place_order(self, symbol, side, qty, order_type, price=None):
        pass

    @abstractmethod
    def get_positions(self):
        pass

    @abstractmethod
    def stream_quotes(self, symbols):
        pass
