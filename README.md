```markdown
# Stock Price Volatility & Portfolio Simulation

## 📌 Project Overview
This project analyzed equity portfolio construction across multiple market regimes using historical return and covariance estimation.

## Project Question & Scope

This project investigates how portfolio construction techniques can be used to balance
return and risk more effectively than naïve allocation strategies using historical stock data.

The analysis focuses on:
- Measuring asset-level volatility and correlation
- Simulating thousands of portfolio allocations
- Evaluating risk-return tradeoffs via the Efficient Frontier
- Identifying portfolios with superior risk-adjusted performance

### Assumptions & Scope
- Historical returns are used as descriptive inputs, not forecasts
- Returns are assumed to be weakly stationary over the analysis window
- Transaction costs and taxes are excluded to isolate portfolio risk dynamics

The goal is not to predict market performance, but to understand structural tradeoffs
in portfolio construction under uncertainty.


The project demonstrates:
- Data sourcing from financial APIs
- Data cleaning & preprocessing
- Volatility analysis (daily returns, rolling windows, VaR)
- Portfolio simulations (Monte Carlo, Sharpe ratio optimization)
- Visualization of key findings (heatmaps, efficient frontier, interactive plots)

---

## 📊 Data Sources
- **Yahoo Finance API (`yfinance`)**
- **Alpha Vantage API** (optional, for extended data)
- **Quandl (NASDAQ)** (optional, additional datasets)
- Market benchmarks: S&P 500, NASDAQ, Dow Jones

---

## 🛠️ Methodology
1. **Data Collection** – Pull historical stock prices (AAPL, MSFT, TSLA, AMZN, JNJ, NVDA).  
2. **Data Cleaning** – Handle missing values, adjust for splits/dividends, format dates.  
3. **Volatility Analysis** – Daily/annualized volatility, rolling windows, Value at Risk.  
4. **Portfolio Simulation** – Monte Carlo simulation of 10,000+ random portfolios, risk-return trade-offs.  
5. **Optimization** – Identify max Sharpe ratio & minimum volatility portfolios.  
6. **Visualization** – Efficient frontier, correlation heatmaps, return distributions.  

---

### Asset Universe
The analysis focuses on six large-cap U.S. equities selected to represent
distinct economic sectors and risk drivers:

- NVDA (Semiconductors / AI Growth)
- MSFT (Enterprise Technology)
- JNJ (Defensive Healthcare)
- JPM (Financials)
- RTX (Industrials & Defense)
- V (Payments & Consumer Transactions)

This universe was chosen to emphasize diversification, correlation structure,
and interpretability rather than return maximization.

### Time Horizon
- Daily data from approximately 2014–2024 (10-year window)

### Benchmark
- S&P 500 Index (^GSPC)

---

## 📈 Key Findings (to be updated as analysis progresses)
* Unconstrained optimization produced extreme concentration (up to 70% NVDA), resulting in severe drawdowns (-55%).

* Introducing a 40% weight cap significantly reduced tail risk while maintaining strong risk-adjusted performance.

* During the COVID shock, correlations increased and volatility spiked, compressing diversification benefits across all portfolios.

* Efficient frontiers shifted materially across regimes, demonstrating that “optimal” portfolios are highly dependent on market conditions.

* Constrained portfolios exhibited more stable allocations and improved resilience under stress.

Strategic Insight

Portfolio optimization under ideal assumptions maximizes theoretical performance but introduces fragility. Incorporating realistic constraints and stress testing across regimes leads to more robust and implementable investment strategies.

---

## 📂 Project Structure
```

data/           # raw & processed stock datasets
notebooks/      # Jupyter notebooks for analysis
src/            # Reusable Python scripts (cleaning, simulation, visualization)
reports/        # Figures and summary documentation

````

---

## 📸 Visualizations
- Stock price trends  
- Rolling volatility  
- Correlation heatmap of returns  
- Efficient frontier with optimal portfolios  

(Example charts to be added here)

---

## 🚀 How to Run
1. Clone the repository  
   ```bash
   git clone https://github.com/USERNAME/stock-volatility-portfolio-simulation.git
   cd stock-volatility-portfolio-simulation
````

2. Create and activate environment

   ```bash
   conda create -n data_env python=3.10 -y
   conda activate data_env
   pip install -r requirements.txt
   ```
3. Run notebooks in `/notebooks`.

---

## 📌 Future Work

* Incorporate **GARCH/ARCH** models for volatility forecasting
* Backtest portfolios against historical performance
* Extend analysis to **crypto and ETFs**
* Build a **Tableau/Power BI dashboard**

---

## ⚙️ Requirements

```
pandas
numpy
matplotlib
seaborn
plotly
yfinance
scipy

```
