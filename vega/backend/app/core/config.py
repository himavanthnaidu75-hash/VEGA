from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    BROKER: str = "paper"
    TOTAL_CAPITAL: float = 100000.0
    MAX_RISK_PER_TRADE: float = 0.01
    MAX_OPEN_POSITIONS: int = 5
    MAX_DAILY_LOSS: float = 0.03
    MAX_DAILY_PROFIT: float = 0.06
    MIN_RR_RATIO: float = 1.5
    POSITION_SIZING: str = "atr"
    TRAILING_SL: bool = True
    TRAILING_SL_ATR_MULTIPLIER: float = 1.5
    TRADING_MODE: str = "SIMULATION"
    WATCHLIST: str = "RELIANCE,TCS,INFY,HDFCBANK,ICICIBANK,SBIN,BHARTIARTL,ITC,ASIANPAINT,TITAN"
    KILL_TOKEN: str = "change_this_before_going_live"
    DATABASE_URL: str = "sqlite:///./vega.db"
    PORT: int = 8000
    class Config: env_file = ".env"

settings = Settings()
