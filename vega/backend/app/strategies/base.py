from abc import ABC, abstractmethod
import pandas as pd
from typing import Optional, Dict

class BaseStrategy(ABC):
    def __init__(self, name: str): self.name = name
    @abstractmethod
    def generate_signal(self, df: pd.DataFrame) -> Optional[Dict]: pass
