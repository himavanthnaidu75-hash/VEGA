import pandas as pd
import numpy as np

class ICTEngine:
    @staticmethod
    def identify_fvgs(df):
        """Identify Fair Value Gaps in a dataframe."""
        fvgs = []
        for i in range(2, len(df)):
            # Bullish FVG: Low of candle 3 > High of candle 1
            if df['High'].iloc[i-2] < df['Low'].iloc[i]:
                fvgs.append({
                    'index': i-1,
                    'type': 'BULLISH',
                    'top': df['Low'].iloc[i],
                    'bottom': df['High'].iloc[i-2],
                    'time': df.index[i-1]
                })
            # Bearish FVG: High of candle 3 < Low of candle 1
            elif df['Low'].iloc[i-2] > df['High'].iloc[i]:
                fvgs.append({
                    'index': i-1,
                    'type': 'BEARISH',
                    'top': df['Low'].iloc[i-2],
                    'bottom': df['High'].iloc[i],
                    'time': df.index[i-1]
                })
        return fvgs

    @staticmethod
    def detect_liquidity_sweep(df, major_levels):
        """
        major_levels: list of prices (PDH, PDL, 52WH, 52WL, etc.)
        """
        if df.empty or not major_levels:
            return False, None

        last_high = df['High'].iloc[-1]
        last_low = df['Low'].iloc[-1]
        last_close = df['Close'].iloc[-1]

        for level in major_levels:
            # Bullish Sweep: Price went below level and closed back above
            if df['Low'].iloc[-1] < level < last_close:
                return True, {"type": "BULLISH", "level": level}
            # Bearish Sweep: Price went above level and closed back below
            if df['High'].iloc[-1] > level > last_close:
                return True, {"type": "BEARISH", "level": level}

        return False, None

    @staticmethod
    def get_market_phase(current_time_ist):
        """Map time to AMD phases."""
        # Assuming current_time_ist is a time object
        t = current_time_ist.hour * 100 + current_time_ist.minute
        if 915 <= t < 1030:
            return "ACCUMULATION"
        elif 1030 <= t < 1230:
            return "MANIPULATION"
        elif 1230 <= t < 1515:
            return "DISTRIBUTION"
        return "OUT_OF_HOURS"

    @staticmethod
    def identify_cisd(df, side="SHORT"):
        """
        Change in State of Delivery.
        For Short: Series of consecutive up-close candles leading to sweep.
        """
        if len(df) < 5: return False

        if side == "SHORT":
            # Find the start of the last up-move
            idx = len(df) - 1
            up_candles = []
            while idx >= 0 and df['Close'].iloc[idx] > df['Open'].iloc[idx]:
                up_candles.append(df.iloc[idx])
                idx -= 1

            if not up_candles: return False

            first_up_open = up_candles[-1]['Open']
            if df['Close'].iloc[-1] < first_up_open:
                return True

        elif side == "LONG":
            idx = len(df) - 1
            down_candles = []
            while idx >= 0 and df['Close'].iloc[idx] < df['Open'].iloc[idx]:
                down_candles.append(df.iloc[idx])
                idx -= 1

            if not down_candles: return False

            first_down_open = down_candles[-1]['Open']
            if df['Close'].iloc[-1] > first_down_open:
                return True

        return False
