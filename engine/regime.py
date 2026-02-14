from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


def detect_regimes(features, n_clusters=3):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(
        features[["market_return", "rolling_vol"]]
    )

    model = KMeans(n_clusters=n_clusters, random_state=42)
    regimes = model.fit_predict(scaled_data)

    features["regime"] = regimes

    # Identify cluster characteristics
    regime_stats = features.groupby("regime")[["market_return", "rolling_vol"]].mean()

    # Label regimes
    labels = {}

    # Highest return = Bull
    bull = regime_stats["market_return"].idxmax()

    # Highest volatility = High Vol
    high_vol = regime_stats["rolling_vol"].idxmax()

    for r in regime_stats.index:
        if r == bull:
            labels[r] = "BULL"
        elif r == high_vol:
            labels[r] = "HIGH_VOL"
        else:
            labels[r] = "BEAR"

    features["regime_label"] = features["regime"].map(labels)

    return features
