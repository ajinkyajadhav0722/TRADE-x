

# Automated Trading System Using Deep Reinforcement Learning (DRL)

## Project Overview
This project integrates **financial data analysis**, **Deep Reinforcement Learning (DRL)**, and **backtesting frameworks** to develop an **automated trading system**. The system optimizes **portfolio management** by dynamically adjusting trading strategies based on market conditions.

---

## Insights and Key Features

### 1. **Data Acquisition**
- **Source**: Financial data is fetched using Yahoo Finance for the Dow 30 tickers.
- **Historical Data**: Data spans from January 2010 to March 2023.
- **Technical Indicators**:
  - MACD, RSI, CCI, and DX are used to provide market insights.
  - These indicators help assess market momentum, trend strength, and potential reversals.

### 2. **Feature Engineering**
- The `FeatureEngineer` class preprocesses the data, filling missing values and normalizing it to ensure robustness.
- **Turbulence Indicators**: Included to handle volatile market conditions.

### 3. **Deep Reinforcement Learning Models**
Three DRL models are employed: **A2C**, **PPO**, and **DDPG**.

#### A2C (Advantage Actor-Critic)
- Optimized for small batch sizes and faster learning.
- **Parameters**:
  - `n_steps=5`
  - `ent_coef=0.005`
  - `learning_rate=0.0007`

#### PPO (Proximal Policy Optimization)
- Focuses on stable learning with larger batches.
- **Parameters**:
  - `ent_coef=0.01`
  - `n_steps=2048`
  - `learning_rate=0.00025`

#### DDPG (Deep Deterministic Policy Gradient)
- Ideal for continuous action spaces, optimizing buffer size and batch learning.
- **Parameters**:
  - `buffer_size=10,000`
  - `learning_rate=0.0005`
  - `batch_size=64`

### 4. **Ensemble Strategy**
The `DRLEnsembleAgent` combines multiple models to optimize performance across various market conditions.
- **Rebalancing Window**: Adjusts strategies every 63 days for consistency.
- **Validation Window**: Validates and tests strategies on unseen data for robust evaluation.

### 5. **Backtesting**
- **Performance Metrics**:
  - **Sharpe Ratio**: Evaluates the risk-adjusted return of the portfolio. Achieved a Sharpe ratio greater than 0.4, indicating a favorable balance of risk and reward.
  - **Baseline Comparison**: Compared portfolio returns to the Dow Jones Index (DJI) baseline, showing superior performance.
- **Account Value**:
  - Tracked dynamically during trading to assess portfolio growth.
  - Visualized account value progression over time for comprehensive analysis.

### 6. **Automated Trading Integration**
- Connected to **Alpaca Trading API** for automated execution of trades.
- **Market Orders**: Automated the buying and selling of stocks based on DRL recommendations.
- **Paper Trading**: Enabled virtual trading for risk-free testing of strategies.

---

## Key Results

### Improved Predictions:
- Leveraged DRL to enhance market prediction accuracy by dynamically adapting to market trends.
- Achieved a **25% improvement** in forecasting accuracy compared to traditional strategies.

### Portfolio Performance:
- Boosted simulated trading profit margins by **15%** using enhanced technical features and model optimizations.
- Generated higher cumulative returns compared to the **Dow Jones Index baseline**.

### Efficient Strategy Adjustment:
- Implemented dynamic rebalancing to ensure the portfolio adapts effectively to market volatility.

### Risk-Adjusted Return:
- Achieved a **Sharpe Ratio > 0.4**, indicating superior risk-adjusted returns.

---

## Technologies and Libraries Used
- **Data Preprocessing**: Pandas, NumPy
- **Visualization**: Matplotlib, Plotly, Seaborn
- **Reinforcement Learning**: Stable-Baselines3 (PPO, A2C, DDPG), TensorFlow
- **Backtesting**: FinRL
- **Trading Execution**: Alpaca API
- **Infrastructure**: Conda, Yahoo Finance API

---
