from engine.data_loader import load_data
from engine.backtester import backtest
from engine.stress_test import apply_market_shock
from engine.metrics import max_drawdown

tickers = ["SPY", "GLD", "TLT"]

data, returns = load_data(tickers, "2015-01-01", "2023-01-01")

# Normal scenario
portfolio_normal = backtest(data, returns, use_risk=True)

# Stress scenario
shocked_returns = apply_market_shock(returns, shock=-0.05)
portfolio_stress = backtest(data, shocked_returns, use_risk=True)

print("Normal Max Drawdown:", max_drawdown(portfolio_normal))
print("Stress Max Drawdown:", max_drawdown(portfolio_stress))
