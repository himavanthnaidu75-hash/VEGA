from .base import BrokerInterface
from .paper import PaperBroker
from ..core.config import settings
from loguru import logger

def get_broker() -> BrokerInterface:
    if settings.BROKER == "paper":
        return PaperBroker(initial_capital=settings.TOTAL_CAPITAL)
    elif settings.BROKER == "dhan":
        from .dhan import DhanBroker
        return DhanBroker()
    elif settings.BROKER == "angel":
        from .angel import AngelOneBroker
        return AngelOneBroker()
    elif settings.BROKER == "zerodha":
        from .zerodha import ZerodhaBroker
        return ZerodhaBroker()
    else:
        logger.warning(f"Unknown broker {settings.BROKER}, falling back to paper.")
        return PaperBroker(initial_capital=settings.TOTAL_CAPITAL)
