import os
import phi
import openai
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app

# Import keys
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
phi.api_key = os.getenv('PHI_API_KEY')

llm_id = "llama3-groq-8b-8192-tool-use-preview"
llm_id = "llama-3.3-70b-versatile"

groq_model = Groq(id=llm_id)

web_search_agent = Agent(
    name="web search agent",
    role="Search web information",
    model=groq_model,
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Finance data agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=groq_model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=False,
            stock_fundamentals=True,
            technical_indicators=True,
            key_financial_ratios=True,
            company_news=True,

        )
    ],
    instructions=["Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[web_search_agent, finance_agent]).get_app()


if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)