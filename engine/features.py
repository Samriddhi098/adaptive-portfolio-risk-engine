import pandas as pd
import numpy as np


def create_features(returns):
    """
    Create rolling return, volatility, and drawdown features.
    """

    features = pd.DataFrame(index=returns.index)

    # Market average return
    features["market_return"] = returns.mean(axis=1)

    # Rolling volatility (20-day)
    features["rolling_vol"] = features["market_return"].rolling(20).std()

    # Rolling mean (momentum)
    features["rolling_mean"] = features["market_return"].rolling(20).mean()

    # Drawdown calculation
    cumulative = (1 + features["market_return"]).cumprod()
    peak = cumulative.cummax()
    features["drawdown"] = (cumulative - peak) / peak

    features = features.dropna()

    return features
