from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

class WebSearchAgent:
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
        """Create the web search agent"""
        return Agent(
            name="web search agent",
            role="Search web information",
            model=self.model,
            tools=[DuckDuckGo()],
            instructions=["Always include sources"],
            show_tool_calls=True,
            markdown=True,
        )

    def search_web(self, query: str):
        """Search the web for information"""
        return self.agent.print_response(query, stream=True)

    def search_news(self, topic: str):
        """Search for news about a specific topic"""
        prompt = f"Search for latest news about {topic}"
        return self.agent.print_response(prompt, stream=True)

# Global instance
web_search_agent = WebSearchAgent()