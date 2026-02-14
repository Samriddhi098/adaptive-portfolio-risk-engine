import numpy as np


def sharpe_ratio(returns):
    return np.sqrt(252) * returns.mean() / returns.std()


def cagr(portfolio_values):
    total_years = len(portfolio_values) / 252
    final_value = portfolio_values.iloc[-1]
    return (final_value ** (1 / total_years)) - 1


def max_drawdown(portfolio_values):
    peak = portfolio_values.cummax()
    drawdown = (portfolio_values - peak) / peak
    return drawdown.min()


def sortino_ratio(returns):
    downside = returns[returns < 0]
    return np.sqrt(252) * returns.mean() / downside.std()
