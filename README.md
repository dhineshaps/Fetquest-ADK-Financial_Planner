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

                      ┌──────────────────────────────────┐
                      │        User / UI / Streamlit       │
                      │   "Analyze my portfolio" Query     │
                      └────────────────────────────────────┘
                                       │
                                       ▼
                     ┌──────────────────────────────────────┐
                     │            ADK Runner                 │
                     │  - Session Management (InMemory)     │
                     │  - Orchestrates the SequentialAgent  │
                     └──────────────────────────────────────┘
                                       │
                                       ▼
         ┌────────────────────────────────────────────────────────────────┐
         │                     SequentialAgent Pipeline                    │
         └────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
     ┌────────────────────┐       ┌────────────────────┐       ┌────────────────────┐
     │  Portfolio Agent    │       │  Rebalance Agent   │       │ Final Summary Agent│
     │ Model: Gemini Flash │       │ Model: Gemini      │       │ Model: Gemini      │
     │ Tools:              │       │ - Reads analysis   │       │ - Human-friendly   │
     │  • get_stock_price  │       │ - Generates BUY/   │       │   final report     │
     │  • analyze_portfolio│       │   SELL / HOLD      │       │                    │
     └────────────────────┘       └────────────────────┘       └────────────────────┘
             │                            │                           │
             ▼                            │                           │
 ┌──────────────────────┐                 │                           │
 │ Python Tools Layer   │                 │                           │
 │  get_stock_price_fn  │                 │                           │
 │  • Normalizes ticker │                 │                           │
 │  • Fetches yfinance  │                 │                           │
 │    live price, vol   │                 │                           │
 │                      │                 │                           │
 │ analyze_portfolio_fn │                 │                           │
 │  • Calculates weights│                 │                           │
 │  • Risk score        │                 │                           │
 │  • Allocation diff   │                 │                           │
 └──────────────────────┘                 │                           │
             │                            │                           │
             ▼                            ▼                           ▼
       (Returns analysis)          (Returns plan)          (Returns summary)
                                       │
                                       ▼
                     ┌──────────────────────────────────────┐
                     │             Final Output              │
                     │  Complete AI-generated portfolio     │
                     │  analysis + rebalancing suggestions  │
                     └──────────────────────────────────────┘


