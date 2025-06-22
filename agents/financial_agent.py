from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

# load_dotenv("../config/.env")

# # Import keys
# groq_api_key = os.getenv('GROQ_API_KEY')
# openai_api_key = os.getenv('OPENAI_API_KEY')
# phi_api_key = os.getenv('PHI_DATA_API_KEY')

class FinancialAgent:
    def __init__(self):
        load_dotenv()
        self.groq_api_key = os.getenv('GROQ_API_KEY')
        self.model = self._setup_model()
        self.agent = self._create_agent()

    def _setup_model(self):
        """Initialize the Groq model"""
        llm_id = "llama-3.3-70b-versatile"
        return Groq(id=llm_id)

    def _create_agent(self):
        """Create the financial analysis agent"""
        return Agent(
            name="Finance AI Agent",
            model=self.model,
            tools=[self._get_yfinance_tools()],
            instructions=["Use table to display the data"],
            show_tool_calls=True,
            markdown=True,
        )

    def _get_yfinance_tools(self):
        """Configure YFinance tools"""
        return YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            technical_indicators=True,
            key_financial_ratios=True,
            company_news=True,
        )

    def analyze_stock(self, ticker: str, analysis_type: str = "comprehensive"):
        """Analyze a specific stock"""
        prompt = f"Analyze {ticker} stock with focus on {analysis_type}"
        return self.agent.print_response(prompt, stream=True)

    def get_analyst_recommendations(self, ticker: str):
        """Get analyst recommendations for a stock"""
        prompt = f"Get analyst recommendations for {ticker}"
        return self.agent.print_response(prompt, stream=True)

    def get_company_news(self, ticker: str):
        """Get latest news for a company"""
        prompt = f"Get latest news for {ticker}"
        return self.agent.print_response(prompt, stream=True)

# Global instance
finance_agent = FinancialAgent()