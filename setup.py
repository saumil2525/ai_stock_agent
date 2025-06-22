from setuptools import setup, find_packages

setup(
    name="financial_ai_agenta",
    version="0.1.0",
    description="Financial AI Agent Project",
    author="Financial agent",
    packages=find_packages(),
    install_requires=[
        "phidata",
        "python-dotenv",
        "yfinance",
        "duckduckgo-search",
        "fastapi",
        "uvicorn",
        "groq",
        "openai"
    ],
    python_requires=">=3.12",
)
