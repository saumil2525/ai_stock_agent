from phi.agent import Agent
from .financial_agent import finance_agent
from .web_search_agent import web_search_agent
from dotenv import load_dotenv
import os

# load_dotenv("../config/.env")

# Import keys
groq_api_key = os.getenv('GROQ_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
phi_api_key = os.getenv('PHI_DATA_API_KEY')

class MultiAgentOrchestrator:
    def __init__(self):
        self.multi_agent = self._create_multi_agent()

    def _create_multi_agent(self):
        """Create multi-agent team"""
        return Agent(
            team=[web_search_agent.agent, finance_agent.agent],
            instructions=["Always include sources", "Use table to display the data"],
            show_tool_calls=True,
            markdown=True,
        )

    def analyze_company_comprehensive(self, ticker: str):
        """Comprehensive company analysis using multiple agents"""
        prompt = f"Summarize analyst recommendations and share the latest news for {ticker}"
        return self.multi_agent.print_response(prompt, stream=True)

    def research_topic(self, topic: str):
        """Research a topic using web search and financial data"""
        prompt = f"Research {topic} including web information and financial data"
        return self.multi_agent.print_response(prompt, stream=True)

# Global instance
multi_agent = MultiAgentOrchestrator()