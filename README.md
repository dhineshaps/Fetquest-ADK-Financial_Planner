# FetQuest -- Multi‑Agent Portfolio Analyzer using Google ADK

## 📌 Overview

FetQuest OneView is an AI‑powered portfolio analysis system built using
the **Google Agent Developer Kit (ADK)**.\
It analyzes your stock portfolio, evaluates allocation vs. target
distribution, computes risk, and provides BUY/SELL/HOLD
actions---powered by a **multi‑agent pipeline**.

This project is developed for the **Kaggle ADK Competition** and
demonstrates: - Multi‑Agent Architecture\
- Python Tools for LLM Agents\
- Sessions & Memory\
- ADK Runners\
- Async Event‑Streaming\
- Gemini LLM Integration

------------------------------------------------------------------------

## 🚀 Features

### ✓ Multi‑Agent System

Your solution includes **three agents** orchestrated with a
`SequentialAgent`: 1. **Portfolio Agent** -- analyzes weights, risk &
allocation differences.\
2. **Rebalance Agent** -- produces BUY / SELL / HOLD recommendations.\
3. **Final Summary Agent** -- generates a clean user-friendly summary.

### ✓ Python Tools (Custom Functions)

Two Python functions are registered as tools: -
`get_stock_price_fn(ticker)` -
`analyze_portfolio_fn(portfolio, target_alloc)`

### ✓ Sessions & Memory

Uses `InMemorySessionService` to manage agent sessions.

### ✓ ADK Runner (Async Event Processing)

Processes agent responses using `runner.run_async()`.

### ✓ Gemini Models

All agents use:

    gemini-2.5-flash-lite

------------------------------------------------------------------------

## 🧠 How It Works (Architecture)

    User Input
       │
       ▼
    Portfolio Agent ──(uses Python tools)──▶ Portfolio Analysis
       │
       ▼
    Rebalance Agent ───────────────────────▶ Buy/Sell/Hold
       │
       ▼
    Final Summary Agent ───────────────────▶ Human‑readable report
       │
       ▼
    Final Output

------------------------------------------------------------------------

## 📂 Project Structure

    agents/
      └── portfolio_runner.py   # Main multi-agent pipeline
    .env                        # Contains GOOGLE_API_KEY
    README.md                   # Project documentation (this file)

------------------------------------------------------------------------

## 🛠 Installation

### 1. Clone the repo

``` bash
git clone https://github.com/<your-repo>/fetquest-oneview-adk.git
cd fetquest-oneview-adk
```

### 2. Create Python environment

``` bash
python -m venv fetquest-env
source fetquest-env/bin/activate   # Windows: fetquest-env\Scripts\activate
```

### 3. Install dependencies

``` bash
pip install google-genai google-adk python-dotenv
```

### 4. Add your API key

Create `.env`:

    GOOGLE_API_KEY=your_key_here

------------------------------------------------------------------------

## ▶ Running the Portfolio Agent

``` bash
python agents/portfolio_runner.py
```

Example output:

    HDFCBANK is over-allocated by 10%
    HDFC is under-allocated by 10%
    TCS is correctly allocated
    Risk Score = 0.156
    Actions → SELL HDFCBANK, BUY HDFC

------------------------------------------------------------------------

## 🌐 Optional: Streamlit UI

You can integrate the multi-agent system with Streamlit:

``` python
import streamlit as st
from portfolio_runner import run_query

query = st.text_input("Ask the Portfolio Planner")

if st.button("Run"):
    result = asyncio.run(run_query(query))
    st.write(result)
```

Deploy to **Streamlit Cloud** for **bonus competition points**.

------------------------------------------------------------------------

## 🧪 Example Prompt

    Portfolio = {"HDFCBANK": 50000, "TCS": 30000, "HDFC": 20000}
    Target = {"HDFCBANK": 0.4, "TCS": 0.3, "HDFC": 0.3}

    Analyze and rebalance.

------------------------------------------------------------------------

