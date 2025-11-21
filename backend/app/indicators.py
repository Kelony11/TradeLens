import yfinance as yf
import pandas as pd


# --------------------------
# Fetch Price Data
# --------------------------

def get_price_series(symbol: str):
    """
    Downloads the last 6 months of daily price data for a given stock symbol.
    Returns the 'Close' price series.
    """
    df = yf.download(symbol, period="6mo", interval="1d", progress=False)
    if df.empty:
        return None
    return df["Close"]


# --------------------------
# Indicator: Simple Moving Average (SMA)
# --------------------------

def compute_sma(series: pd.Series, window: int):
    """
    Computes the Simple Moving Average (SMA) over a rolling window.
    """
    return series.rolling(window=window).mean()


# --------------------------
# Simple Trading Signal Logic
# --------------------------

def simple_signal(symbol: str) -> str:
    """
    Simple BUY/SELL/HOLD signal based on SMA crossover:
    - BUY  = SMA20 > SMA50
    - SELL = SMA20 < SMA50
    - HOLD = otherwise
    """

    series = get_price_series(symbol)

    if series is None or len(series) < 50:
        return "HOLD"

    sma_fast = compute_sma(series, 20).iloc[-1]
    sma_slow = compute_sma(series, 50).iloc[-1]

    if sma_fast > sma_slow:
        return "BUY"
    elif sma_fast < sma_slow:
        return "SELL"
    else:
        return "HOLD"
