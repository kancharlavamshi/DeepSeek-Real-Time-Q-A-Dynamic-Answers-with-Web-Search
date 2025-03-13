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

This project, **DeepSeek Real-Time Q&A**, is developed solely for **educational purposes** to demonstrate the integration of real-time web search (via DuckDuckGo) with AI-powered responses (via DeepSeek and OpenRouter). It is not intended for commercial use, production deployment, or any purpose beyond personal learning and experimentation.

- **Usage**: Users are responsible for obtaining their own OpenRouter API key and adhering to the [OpenRouter Terms of Service](https://openrouter.ai/terms). Excessive or unauthorized use of the API may violate these terms.
- **Third-Party Services**: This project relies on the `duckduckgo_search` library (MIT License) and the `openai` library (MIT License), as well as DuckDuckGo’s search functionality. Users must comply with DuckDuckGo’s policies and any applicable rate limits.
- **No Warranty**: The code is provided "as is" without any warranties, express or implied. The author is not liable for any damages, errors, or issues arising from its use.
- **Educational Intent**: This is a learning tool, not a finished product. It may contain limitations or bugs typical of a demonstration project.

By using this project, you agree to respect the terms of all referenced services and use it responsibly within the scope of educational exploration.


