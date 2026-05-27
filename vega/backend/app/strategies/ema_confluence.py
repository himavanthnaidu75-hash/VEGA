from .base import BaseStrategy
from ..utils.indicators import ema
import pandas as pd
from typing import Optional, Dict

class EMAConfluenceStrategy(BaseStrategy):
    def __init__(self): super().__init__("EMA Confluence")
    def generate_signal(self, df: pd.DataFrame) -> Optional[Dict]:
        if len(df) < 200: return None
        e9, e21, e50, e200 = ema(df['Close'], 9), ema(df['Close'], 21), ema(df['Close'], 50), ema(df['Close'], 200)
        last_close = df['Close'].iloc[-1]
        if e9.iloc[-1] > e21.iloc[-1] > e50.iloc[-1] > e200.iloc[-1] and last_close <= e21.iloc[-1] * 1.005:
            return {'side': 'BUY', 'entry': last_close, 'sl': e50.iloc[-1], 'tp': last_close * 1.05}
        return None
