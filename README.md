# DeepSeek Real-Time Q&A: Dynamic Answers with Web Search

**Note**: This project is developed for **educational purposes** to demonstrate the integration of real-time web search (DuckDuckGo) with AI-powered responses (DeepSeek via OpenRouter). It is not intended for commercial use or large-scale deployment.

## Overview
This script combines DuckDuckGo search with DeepSeek’s AI to answer user queries with up-to-date info. It’s a learning tool for exploring API usage, search integration, and natural language processing.

## Setup
1. Clone the repo: `https://github.com/kancharlavamshi/DeepSeek-Real-Time-Q-A-Dynamic-Answers-with-Web-Search.git`
2. Install dependencies: `pip install openai duckduckgo-search`
3. Set your OpenRouter API key as an environment variable:
   ```bash
   export OPENROUTER_API_KEY="your-key-here"

## Features
- **Real-Time Search**: Fetches the latest information from the web using DuckDuckGo, filtered to exclude irrelevant pages (e.g., login/signup).
- **AI-Powered Responses**: Leverages DeepSeek’s natural language understanding to craft detailed, coherent answers.
- **Customizable Queries**: Users can ask anything, and the system dynamically adapts to provide relevant context.
- **Lightweight & Fast**: Built with minimal dependencies for quick setup and execution.

## How It Works
1. User inputs a question.
2. The system searches the web for the latest info using DuckDuckGo, constrained to results after March 1, 2025.
3. DeepSeek processes the search context and generates a comprehensive response, capped at 500 tokens.



## Run

python deepseek_realtime_qa.py


## Disclaimer
Uses the openai library (MIT License), duckduckgo_search (MIT License), and OpenRouter’s free tier.
Please adhere to the Terms of Service of all services used.
For educational use only—do not deploy in production without permission from service providers.



