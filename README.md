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

