from ..base import BaseStrategy
import pandas as pd
from ...utils.indicators import *

class Strategy_3_11Strategy(BaseStrategy):
    def __init__(self): super().__init__("Single moving average . . . . . . . . . . . . . . . . . . . . .       49")
    def generate_signal(self, df):
        if len(df) < 50: return None
        try:
            # Using formula 1
            res = f_1(ST=df['Close'].iloc[-1], S0=df['Close'].iloc[0], K=df['Close'].iloc[-1], C=1.0, D=1.0, K1=df['Close'].iloc[-1], K2=df['Close'].iloc[-1])
            if res > 0: return {'side': 'BUY', 'entry': df['Close'].iloc[-1], 'sl': df['Close'].iloc[-1]*0.98, 'tp': df['Close'].iloc[-1]*1.05, 'confidence_boost': 5}
        except: pass
        return None
