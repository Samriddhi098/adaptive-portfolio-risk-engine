import numpy as np


def volatility_scaling(portfolio_returns, target_vol=0.12, window=20):
    """
    Scale exposure to maintain target annualized volatility.
    """

    if len(portfolio_returns) < window:
        return 1  # Not enough data yet

    rolling_vol = portfolio_returns[-window:].std() * np.sqrt(252)

    if rolling_vol == 0:
        return 1

    scaling_factor = target_vol / rolling_vol

    # Avoid extreme leverage
    return min(scaling_factor, 1)


def drawdown_scaling(portfolio_values):
    """
    Reduce exposure when drawdown exceeds thresholds.
    """

    peak = portfolio_values.cummax()
    drawdown = (portfolio_values - peak) / peak

    latest_dd = drawdown.iloc[-1]

    if latest_dd < -0.10:
        return 0.6
    elif latest_dd < -0.05:
        return 0.8
    else:
        return 1
