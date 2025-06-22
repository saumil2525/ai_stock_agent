from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()
        self.groq_api_key = os.getenv('GROQ_API_KEY')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.phi_api_key = os.getenv('PHI_API_KEY')

        # Model configurations
        self.default_llm_id = "llama-3.3-70b-versatile"
        self.fallback_llm_id = "llama3-groq-8b-8192-tool-use-preview"

        # Agent configurations
        self.default_instructions = ["Always include sources", "Use table to display the data"]

    def validate_keys(self):
        """Validate that required API keys are present"""
        required_keys = ['GROQ_API_KEY']
        missing_keys = [key for key in required_keys if not os.getenv(key)]

        if missing_keys:
            raise ValueError(f"Missing required API keys: {missing_keys}")

        return True

# Global config instance
config = Config()