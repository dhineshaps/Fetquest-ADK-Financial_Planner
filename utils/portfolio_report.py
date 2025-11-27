import streamlit as st

def portfolio_report(report: dict):
    """
    Display a clean, structured portfolio report.

    Expected dict format:
    {
        "current": {"HDFCBANK": 50000, "TCS": 30000, "HDFC": 20000},
        "target": {"HDFCBANK": 0.4, "TCS": 0.3, "HDFC": 0.3},
        "actual": {"HDFCBANK": 0.5, "TCS": 0.3, "HDFC": 0.2},
        "risk_score": 0.156,
        "analysis": ["point 1", "point 2"],
        "recommended_actions": ["Sell HDFCBANK", "Buy HDFC"]
    }
    """

    st.markdown("## 📊 Portfolio Rebalancing Summary")


    st.markdown("### 💼 Current Portfolio")
    for asset, value in report.get("current", {}).items():
        st.write(f"- **{asset}**: ₹{value:,}")

  
    st.markdown("---")
    st.markdown("### 🎯 Target Allocation")
    for asset, pct in report.get("target", {}).items():
        st.write(f"- **{asset}**: {pct*100:.1f}%")

 
    st.markdown("---")
    st.markdown("### 📈 Actual Allocation")
    for asset, pct in report.get("actual", {}).items():
        st.write(f"- **{asset}**: {pct*100:.1f}%")


    st.markdown("---")
    st.metric(label="⚠️ Risk Score", value=f"{report.get('risk_score', 0):.3f}")


    st.markdown("---")
    st.markdown("### 🔍 Analysis")
    for point in report.get("analysis", []):
        st.write(f"- {point}")


    st.markdown("---")
    st.markdown("### 🔄 Recommended Actions")

    for action in report.get("recommended_actions", []):
        if action.lower().startswith("buy"):
            st.success(f"🟢 {action}")
        elif action.lower().startswith("sell"):
            st.error(f"🔴 {action}")
        else:
            st.info(f"⚪ {action}")
