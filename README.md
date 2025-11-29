# FetQuest -- Multi‑Agent Portfolio Analyzer using Google ADK

## 📌 Overview

FetQuest OneView is an AI‑powered Stock portfolio analysis system built using
the **Google Agent Developer Kit (ADK)**.\
It analyzes your stock portfolio, evaluates allocation vs. target
distribution, computes risk, and provides BUY/SELL/HOLD
actions---powered by a **multi‑agent pipeline**.

This project is developed for the **Kaggle ADK Competition** and
demonstrates: - Multi‑Agent Architecture 
- Python Tools for LLM Agents
- Sessions & Memory
- ADK Runners
- Async Event‑Streaming
- Gemini LLM Integration

------------------------------------------------------------------------

## Features

### Multi‑Agent System

Your solution includes **three agents** orchestrated with a
`SequentialAgent`: 1. **Portfolio Agent** -- analyzes weights, risk &
allocation differences.\
2. **Rebalance Agent** -- produces BUY / SELL / HOLD recommendations.\
3. **Final Summary Agent** -- generates a clean user-friendly summary.

### Python Tools (Custom Functions)

Two Python functions are registered as tools: -
`get_stock_price_fn(ticker)` -
`analyze_portfolio_fn(portfolio, target_alloc)`

### Sessions & Memory

Uses `InMemorySessionService` to manage agent sessions.

### ADK Runner (Async Event Processing)

Processes agent responses using `runner.run_async()`.

###  Gemini Models

All agents use:

    gemini-2.5-flash-lite

------------------------------------------------------------------------
## Architecture diagram

![FET ADK Agents Architecture](https://raw.githubusercontent.com/dhineshaps/Fetquest-ADK-Financial_Planner/main/FET%20ADK%20Agents.png)

      



