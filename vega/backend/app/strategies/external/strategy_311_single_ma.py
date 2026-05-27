from ..base import BaseStrategy
from ...utils.indicators import sma
import pandas as pd
from typing import Optional, Dict

class SingleMAStrategy(BaseStrategy):
    def __init__(self, period: int = 20): super().__init__(f"Single MA ({period})")
    def generate_signal(self, df: pd.DataFrame) -> Optional[Dict]:
        if len(df) < 20: return None
        ma = sma(df['Close'], 20)
        if df['Close'].iloc[-1] > ma.iloc[-1] and df['Close'].iloc[-2] <= ma.iloc[-2]:
            return {'side': 'BUY', 'entry': df['Close'].iloc[-1], 'sl': df['Close'].iloc[-1] * 0.98, 'tp': df['Close'].iloc[-1] * 1.05}
        return None
