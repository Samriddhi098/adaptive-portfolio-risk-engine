import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from engine.data_loader import load_data
from engine.backtester import backtest
from engine.metrics import sharpe_ratio, cagr, max_drawdown
from engine.stress_test import apply_market_shock


st.set_page_config(layout="wide")
st.title("Autonomous Adaptive Portfolio & Risk Management Engine")

# Sidebar controls
st.sidebar.header("Configuration")

start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2015-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-01-01"))

use_risk = st.sidebar.checkbox("Enable Risk Engine", value=True)

shock_level = st.sidebar.slider("Stress Shock (%)", -0.2, 0.0, -0.05)

tickers = ["SPY", "GLD", "TLT"]

if st.button("Run Backtest"):

    data, returns = load_data(tickers, str(start_date), str(end_date))
    st.write("First 5 Returns:")
    st.write(returns.head())

    portfolio_with_risk = backtest(data, returns, use_risk=True)
    portfolio_no_risk = backtest(data, returns, use_risk=False)

    shocked_returns = apply_market_shock(returns, shock=shock_level)
    portfolio_stress = backtest(data, shocked_returns, use_risk=True)

    st.subheader("Portfolio Growth Comparison")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(portfolio_with_risk, label="With Risk Engine")
    ax.plot(portfolio_no_risk, label="Without Risk Engine")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Stress Test Scenario")

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(portfolio_stress, label="Stress Scenario (With Risk)")
    ax2.legend()
    st.pyplot(fig2)

    st.subheader("Performance Metrics")

    returns_with_risk = portfolio_with_risk.pct_change().dropna()

    col1, col2, col3 = st.columns(3)

    col1.metric("Final Value", round(portfolio_with_risk.iloc[-1], 2))
    col2.metric("Sharpe Ratio", round(sharpe_ratio(returns_with_risk), 2))
    col3.metric("Max Drawdown", round(max_drawdown(portfolio_with_risk), 2))

    st.success("Backtest Completed Successfully.")
