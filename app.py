import streamlit as st
import asyncio
from agents.portfolio_runner import run_query
from utils.portfolio_report import portfolio_report

st.title("📊 FetQuest Portfolio Analyzer")

portfolio = {"HDFCBANK": 50000, "TCS": 30000, "HDFC": 20000}
target = {"HDFCBANK": 0.4, "TCS": 0.3, "HDFC": 0.3}

if st.button("Analyze Portfolio"):
    query = f"Portfolio={portfolio}, Target={target}. Analyze and rebalance."

    with st.spinner("Analyzing…"):
        result = asyncio.run(run_query(query))

    st.subheader("Raw Final Output")
    st.code(result)
