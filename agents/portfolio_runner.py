import asyncio
from google import genai
from google.genai import types
#from google.adk import session
import os
import asyncio
from dotenv import load_dotenv

from google.adk.agents import Agent, SequentialAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

from google.genai import types
from google import genai

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)


def get_stock_price_fn(ticker: str):
    prices = {
        "HDFCBANK": {"price": 1620, "volatility": 0.18},
        "TCS": {"price": 3890, "volatility": 0.12},
        "HDFC": {"price": 3000, "volatility": 0.15},
    }

    if ticker.upper() in prices:
        return {"status": "success", "result": prices[ticker.upper()]}
    return {"status": "error", "error_message": f"{ticker} not found"}


def analyze_portfolio_fn(portfolio: dict, target_alloc: dict):
    total = sum(portfolio.values())
    weights = {t: portfolio[t] / total for t in portfolio}

    # weighted risk
    risk = 0
    for t in portfolio:
        res = get_stock_price_fn(t)
        if res["status"] == "success":
            risk += weights[t] * res["result"]["volatility"]

    diff = {t: target_alloc.get(t, 0) - weights[t] for t in portfolio}

    return {
        "status": "success",
        "weights": weights,
        "risk_score": risk,
        "allocation_diff": diff,
    }

portfolio_agent = Agent(
    name="portfolio_agent",
    model="gemini-2.5-flash-lite",
    instruction="""
    You are the Portfolio Analysis Agent.
    You have 2 python tools:
    1) get_stock_price_fn(ticker)
    2) analyze_portfolio_fn(portfolio, target_alloc)

    Use them when needed and return a short analysis.
    """,
    tools=[get_stock_price_fn, analyze_portfolio_fn],
)

rebalance_agent = Agent(
    name="rebalance_agent",
    model="gemini-2.5-flash-lite",
    instruction="""
    You are the Rebalancing Agent.
    Based on the portfolio analysis (weights + diff), give BUY/SELL/HOLD.
    Return plain text.
    """,
)

final_agent = Agent(
    name="final_summary_agent",
    model="gemini-2.5-flash-lite",
    instruction="""
    Combine all previous outputs into one clean summary.
    No JSON. Only user-friendly text.
    """,
)

system = SequentialAgent(
    name="financial_planner",
    sub_agents=[portfolio_agent, rebalance_agent, final_agent],
)


APP_NAME = "FetQuest-OneView"
USER_ID = "user123"
SESSION_ID = "s1"

async def get_runner():
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    return Runner(agent=system, app_name=APP_NAME, session_service=session_service)



async def run_query(query: str) -> str:
    runner = await get_runner()

    content = types.Content(
        role="user",
        parts=[types.Part(text=query)]
    )

    final_output = ""

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=content
    ):
        if event.is_final_response():
            final_output = event.content.parts[0].text

    return final_output


if __name__ == "__main__":
    portfolio = {"HDFCBANK": 50000, "TCS": 30000, "HDFC": 20000}
    target = {"HDFCBANK": 0.4, "TCS": 0.3, "HDFC": 0.3}
    prompt = f"Portfolio={portfolio}, Target={target}. Analyze and rebalance."

    result = asyncio.run(run_query(prompt))

    print("\n=== FINAL OUTPUT ===\n")
    print(result)
