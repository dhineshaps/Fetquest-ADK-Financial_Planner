FetQuest – Financial Planner Agent (ADK Competition)

This project is my submission for the Kaggle AI DevKit (ADK) Capstone Competition.
It demonstrates a multi-agent system, custom Python tools, session memory, and agent orchestration using Google’s ADK Runners & Sequential Agents.

The system performs:
Portfolio analysis
Risk evaluation
Portfolio rebalancing
Final human-readable summary

All powered by Gemini 2.5 Flash-Lite agents.

Features:
Three-Agent Multi-Agent Pipeline:
   Implemented using SequentialAgent:

Portfolio Agent

Uses Python tools

Fetches static stock prices

Computes weights, risk, and allocation delta

Rebalancing Agent

Interprets analysis results

Generates BUY/SELL/HOLD guidance

3)Final Summary Agent

  Combines previous outputs
  Returns clean, user-friendly text
