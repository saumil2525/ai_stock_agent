from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import openai
import os

load_dotenv()

# Import keys
groq_api_key = os.getenv('GROQ_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
phi_api_key = os.getenv('PHI_API_KEY')

print(groq_api_key)


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
            analyst_recommendations=True,
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

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Alway include sources", "Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)


# get response
company_tickr = "NVDA"
promt_tickr = f"Summerize analyst recommendations and share the latest new for the {company_tickr}"

# multi_ai_agent.model = groq_model  # Set Groq model explicitly

multi_ai_agent.print_response(promt_tickr, stream=True)

