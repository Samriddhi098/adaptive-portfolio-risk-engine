# Autonomous Adaptive Portfolio & Risk Management Engine

## 📌 Overview

This project implements an **Autonomous Adaptive Portfolio & Risk Management Engine** that dynamically adjusts asset allocation based on market regimes and risk conditions to optimize long-term risk-adjusted returns while protecting capital during volatility and crisis periods.

Unlike traditional trading systems, this engine focuses on:

- Regime detection
- Dynamic asset allocation
- Volatility targeting
- Drawdown protection
- Stress testing
- Walk-forward backtesting

---

## 🧠 Core Philosophy

Markets evolve through different regimes:

- Bull Markets (Low Volatility, Positive Returns)
- Bear Markets (Negative Returns)
- High Volatility / Crisis Periods

This system automatically:

- Detects market regime using KMeans clustering
- Allocates capital using inverse volatility weighting
- Adjusts exposure dynamically using risk scaling
- Protects capital during stress scenarios

---

## 🏗 System Architecture
User Interface (Streamlit)
↓
Backtest Engine
↓
Regime Detection (KMeans)
↓
Inverse Volatility Allocation
↓
Risk Engine
├── Volatility Targeting
└── Drawdown Scaling
↓
Portfolio Simulation
↓
Performance Metrics + Stress Testing

---

## 🔄 Execution Flow

1. Load historical market data (SPY, GLD, TLT)
2. Compute rolling features (volatility, returns, drawdown)
3. Detect regimes using KMeans clustering
4. Allocate weights using inverse volatility
5. Adjust exposure using risk engine
6. Simulate portfolio performance (walk-forward)
7. Evaluate metrics (Sharpe, CAGR, Max Drawdown)
8. Run stress testing scenarios
9. Display results in Streamlit dashboard

---

## 📊 Features

- ✅ KMeans Regime Detection
- ✅ Inverse Volatility Allocation
- ✅ Regime-adjusted exposure
- ✅ Volatility Targeting
- ✅ Drawdown-based scaling
- ✅ Walk-forward backtesting
- ✅ Stress Testing Simulation
- ✅ With vs Without Risk Comparison
- ✅ Interactive Streamlit Dashboard

---

## 🧪 Stress Testing

The system simulates:

- Market shocks (-5% to -20%)
- Volatility spikes
- Crisis scenarios

This demonstrates capital protection capability.

---

## 📈 Performance Metrics

- Sharpe Ratio
- CAGR
- Max Drawdown
- Sortino Ratio
- Risk vs No-Risk comparison

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn (KMeans)
- yFinance
- Streamlit
- Matplotlib

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/adaptive-portfolio-risk-engine.git
cd adaptive-portfolio-risk-engine

2️⃣Create Virtual Environment
Windows:

python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run Application
streamlit run app.py

📂 Project Structure
adaptive_portfolio_engine/
│
├── app.py
├── requirements.txt
│
└── engine/
    ├── data_loader.py
    ├── features.py
    ├── regime.py
    ├── allocation.py
    ├── risk.py
    ├── backtester.py
    ├── metrics.py
    ├── stress_test.py
    ├── explain.py
