import pandas as pd
from sklearn.preprocessing import scale
from engine.features import create_features
from engine.regime import detect_regimes
from engine.allocation import inverse_volatility_weights, regime_adjusted_weights
from engine.risk import volatility_scaling, drawdown_scaling


def backtest(data, returns, use_risk=True):

    portfolio_value = [1]
    portfolio_returns = []

    for i in range(60, len(returns)):

        window_returns = returns.iloc[:i]

        # Regime detection
        features = create_features(window_returns)
        features = detect_regimes(features)
        current_regime = features["regime_label"].iloc[-1]

        # Allocation
        base_weights = inverse_volatility_weights(window_returns)
        weights = regime_adjusted_weights(base_weights, current_regime)

        daily_return = (returns.iloc[i] * weights).sum()

        scale = 1  # default no scaling

        if use_risk:

            # Temporary portfolio series for risk calculation
            temp_returns = pd.Series(portfolio_returns + [daily_return])
            temp_value = pd.Series(portfolio_value + [
                portfolio_value[-1] * (1 + daily_return)
            ])

            vol_scale = volatility_scaling(temp_returns)
            dd_scale = drawdown_scaling(temp_value)

            scale = vol_scale * dd_scale
            print("Scale:", scale)

        adjusted_return = daily_return * scale

        temp_returns = pd.Series(portfolio_returns + [daily_return])


        new_value = portfolio_value[-1] * (1 + adjusted_return)
        portfolio_value.append(new_value)

    portfolio_series = pd.Series(portfolio_value[1:], index=returns.index[60:])

    return portfolio_series

