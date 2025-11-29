import streamlit as st
import asyncio
import pandas as pd
from agents.portfolio_runner import run_query
from utils.portfolio_report import portfolio_report

st.markdown("<h1 style='text-align: center; color: #DAA520;font-size: 35px'>The FET Quest - OneView</h1>", unsafe_allow_html=True)

st.title("📊 AI Stock Portfolio Analyzer")

st.write("Enter your stocks, current value, and target weights (%).")


default_data = {
    "Asset": ["HDFC","ITC"],
    "Current Value": [50000,4000],
    "Target %": [40,60]
}

df = st.data_editor(
    pd.DataFrame(default_data),
    num_rows="dynamic",
    key="portfolio_editor"
)

total_weight = df["Target %"].sum()

if total_weight != 100:
    st.warning(f"⚠️ Target weights must add up to 100%. Current total = {total_weight}%", icon="⚠️")
else:
    st.success("✅ Target weights sum to 100%.")

#converting to dict
portfolio = dict(zip(df["Asset"], df["Current Value"]))
print(portfolio)

#calculating percentage from real value
target = {row["Asset"]: row["Target %"] / 100 for _, row in df.iterrows()}
print(target)


#ADK Analaysis
if st.button("Analyze Portfolio"):
    if total_weight != 100:
        st.error("❌ Cannot analyze: Target % must equal 100%.")
    else:
        query = f"Portfolio={portfolio}, Target={target}. Analyze and rebalance."

        with st.spinner("Analyzing…"):
            result = asyncio.run(run_query(query))

        st.subheader("AI Suggestion")
        st.code(result)
