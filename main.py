#!/usr/bin/env python3
"""
Main entry point for the AI Agent application.
"""

from config.settings import config
from agents.financial_agent import finance_agent
from agents.web_search_agent import web_search_agent
from agents.multi_agent import multi_agent
from utils.helpers import print_separator, validate_ticker
from dotenv import load_dotenv
import os

# Import keys
load_dotenv("../config/.env")
groq_api_key = os.getenv('GROQ_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')
phi_api_key = os.getenv('PHI_DATA_API_KEY')

def main():
    """Main application function."""
    print_separator("AI Agent Application Starting...")

    # Validate configuration
    try:
        config.validate_keys()
        print("✓ Configuration validated")
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        return

    # Example usage
    ticker = "NVDA"
    if validate_ticker(ticker):
        print_separator(f"Analyzing {ticker}")
        multi_agent.analyze_company_comprehensive(ticker)
    else:
        print(f"❌ Invalid ticker: {ticker}")

if __name__ == "__main__":
    main()