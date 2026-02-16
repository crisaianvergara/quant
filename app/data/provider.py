from abc import ABC, abstractmethod
import pandas as pd


class DataProvider(ABC):
    @abstractmethod
    def get_daily_bars(self, symbol: str) -> pd.DataFrame:
        pass
