import numpy as np


def inverse_volatility_weights(returns, window=20):
    rolling_vol = returns.rolling(window).std().iloc[-1]
    rolling_vol = rolling_vol.replace(0, np.nan)

    inv_vol = 1 / rolling_vol
    weights = inv_vol / inv_vol.sum()

    return weights


def regime_adjusted_weights(weights, regime_label):
    """
    Modify base weights depending on regime.
    """

    adjusted = weights.copy()

    if regime_label == "BULL":
        adjusted *= 1.2  # increase exposure
    elif regime_label == "BEAR":
        adjusted *= 0.8  # reduce exposure
    elif regime_label == "HIGH_VOL":
        adjusted *= 0.6  # reduce more

    adjusted = adjusted / adjusted.sum()

    return adjusted
