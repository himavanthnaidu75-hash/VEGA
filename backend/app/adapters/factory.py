from .paper import PaperAdapter
from .dhan import DhanAdapter
import os

def get_broker_adapter(adapter_type="PAPER", **kwargs):
    if adapter_type == "DHAN":
        return DhanAdapter(
            client_id=os.getenv("DHAN_CLIENT_ID"),
            access_token=os.getenv("DHAN_ACCESS_TOKEN")
        )
    return PaperAdapter()
