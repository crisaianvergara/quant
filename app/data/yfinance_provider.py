import yfinance_provider as yf
from pathlib import Path
from .provider import DataProvider

DATA_DIR = Path("storage/market_data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


class YFinanceProvider(DataProvider):
    def get_daily_bars(self, symbol: str):
        file = DATA_DIR / f"{symbol}.csv"

        if file.exists():
            return yf.download(symbol, period="max", auto_adjust=True)

        df = yf.download(symbol, period="max", auto_adjust=True)
        df = df[["Open", "High", "Low", "Close", "Volume"]]
        df.to_csv(file)

        return df
