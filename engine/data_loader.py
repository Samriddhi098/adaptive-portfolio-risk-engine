import yfinance as yf
import pandas as pd


def load_data(tickers, start_date, end_date):
    """
    Download price data and compute daily returns.
    """

    data = yf.download(tickers, start=start_date, end=end_date)

    # If multi-level columns exist
    if isinstance(data.columns, pd.MultiIndex):
        if "Adj Close" in data.columns.levels[0]:
            data = data["Adj Close"]
        else:
            data = data["Close"]
    else:
        data = data["Adj Close"] if "Adj Close" in data.columns else data["Close"]

    data = data.dropna()

    returns = data.pct_change().dropna()

    return data, returns
