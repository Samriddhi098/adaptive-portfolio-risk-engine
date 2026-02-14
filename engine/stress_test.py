import pandas as pd


def apply_market_shock(returns, shock=-0.05):
    """
    Apply a uniform negative shock to returns.
    """
    shocked_returns = returns.copy()
    shocked_returns += shock
    return shocked_returns


def apply_volatility_spike(returns, multiplier=2):
    """
    Increase volatility artificially.
    """
    shocked_returns = returns * multiplier
    return shocked_returns
