import asyncio
import pandas as pd
from typing import List, Dict, Optional
from loguru import logger
from ..services.data_service import DataService

class Scanner:
    def __init__(self, watchlist: List[str]):
        self.watchlist = watchlist
        self.data_cache: Dict[str, Dict[str, pd.DataFrame]] = {}

    async def scan_all(self) -> Dict[str, Dict[str, pd.DataFrame]]:
        """
        Fetches multi-timeframe data for all symbols in watchlist.
        Returns: { 'RELIANCE': { '5m': df, '15m': df, '1h': df, '1d': df } }
        """
        results = {}
        for symbol in self.watchlist:
            try:
                # Multi-timeframe fetch
                tf_data = {
                    '1m': DataService.fetch_ohlcv(symbol, interval="1m", period="2d"),
                    '5m': DataService.fetch_ohlcv(symbol, interval="5m", period="5d"),
                    '15m': DataService.fetch_ohlcv(symbol, interval="15m", period="10d"),
                    '1h': DataService.fetch_ohlcv(symbol, interval="1h", period="30d"),
                    '1d': DataService.fetch_ohlcv(symbol, interval="1d", period="1y")
                }
                # Filter empty data
                if not tf_data['5m'].empty:
                    results[symbol] = tf_data
            except Exception as e:
                logger.error(f"Scanner error for {symbol}: {e}")

        self.data_cache = results
        return results

    def get_cached_data(self, symbol: str, timeframe: str) -> Optional[pd.DataFrame]:
        return self.data_cache.get(symbol, {}).get(timeframe)
