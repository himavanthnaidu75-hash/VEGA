import pandas as pd
import pandas_ta as ta
from .ict_engine import ICTEngine

class StrategyEngine:
    def __init__(self, data_service):
        self.data_service = data_service

    def generate_signals(self, symbol, htf_df, ltf_df, major_levels):
        """
        htf_df: Higher Timeframe (15m/1h)
        ltf_df: Lower Timeframe (1m/5m)
        """
        signals = []

        # 1. ICT Checks
        # Step 1: Liquidity Sweep on LTF
        swept, sweep_info = ICTEngine.detect_liquidity_sweep(ltf_df, major_levels)
        if not swept:
            return signals

        # Step 2: HTF FVG Confirmation
        htf_fvgs = ICTEngine.identify_fvgs(htf_df)
        last_price = ltf_df['Close'].iloc[-1]

        in_htf_fvg = False
        for fvg in htf_fvgs:
            if fvg['bottom'] <= last_price <= fvg['top']:
                if (sweep_info['type'] == 'BULLISH' and fvg['type'] == 'BULLISH') or                    (sweep_info['type'] == 'BEARISH' and fvg['type'] == 'BEARISH'):
                    in_htf_fvg = True
                    break

        if not in_htf_fvg:
            return signals

        # Step 3: CISD Confirmation
        cisd_confirmed = ICTEngine.identify_cisd(ltf_df, side="LONG" if sweep_info['type'] == 'BULLISH' else "SHORT")
        if not cisd_confirmed:
            return signals

        # 2. Indicator Confirmation (Secondary Filters)
        ltf_df.ta.ema(length=9, append=True)
        ltf_df.ta.ema(length=21, append=True)
        ltf_df.ta.rsi(length=14, append=True)

        ema_9 = ltf_df['EMA_9'].iloc[-1]
        ema_21 = ltf_df['EMA_21'].iloc[-1]
        rsi = ltf_df['RSI_14'].iloc[-1]

        indicator_pass = False
        if sweep_info['type'] == 'BULLISH':
            if last_price > ema_9 > ema_21 and rsi > 50:
                indicator_pass = True
        else:
            if last_price < ema_9 < ema_21 and rsi < 50:
                indicator_pass = True

        if indicator_pass:
            signals.append({
                'symbol': symbol,
                'side': 'BUY' if sweep_info['type'] == 'BULLISH' else 'SELL',
                'price': last_price,
                'type': 'ICT_CONFIRMED',
                'timestamp': ltf_df.index[-1]
            })

        return signals
