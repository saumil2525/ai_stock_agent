import os
from typing import Optional

def validate_ticker(ticker: str) -> bool:
    """Validate stock ticker format"""
    if not ticker or len(ticker) > 10:
        return False
    return ticker.isalnum()

def format_prompt(ticker: str, analysis_type: str) -> str:
    """Format analysis prompts consistently"""
    return f"Analyze {ticker.upper()} with focus on {analysis_type}"

def get_env_var(key: str, default: Optional[str] = None) -> Optional[str]:
    """Safely get environment variable"""
    return os.getenv(key, default)

def print_separator(title: str = ""):
    """Print a formatted separator"""
    print(f"\n{'='*50}")
    if title:
        print(f" {title}")
        print(f"{'='*50}\n")