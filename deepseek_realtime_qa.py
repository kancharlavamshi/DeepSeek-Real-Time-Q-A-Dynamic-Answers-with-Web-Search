import os
from openai import OpenAI
from duckduckgo_search import DDGS

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")  # Set your key in environment variables
)

def get_latest_info(user_query):
    """Fetch real-time info from DuckDuckGo."""
    search_query = f"{user_query} -inurl:(signup login) after:2025-03-01"
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(search_query, max_results=10, timelimit="m"))
        info = ""
        for result in results:
            info += f"{result['title']} - {result['body'][:300]}... "
            if len(info) > 500:
                break
        return info if info else f"No latest info found for '{user_query}' as of March 13, 2025."
    except Exception as e:
        return f"Error fetching info: {str(e)}"

user_question = input("Ask anything: ")
latest_info_context = get_latest_info(user_question)
print("Latest Info Context:", latest_info_context)

prompt = (
    f"Using the following context: '{latest_info_context}', "
    f"provide a detailed response to: '{user_question}'. Include relevant details "
    f"like early life, career, family, achievements, and latest updates where applicable."
)

try:
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat:free",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.6,
        top_p=0.85
    )
    print("\nResponse:")
    print(response.choices[0].message.content.strip())
except Exception as e:
    print(f"Error generating response: {str(e)}")
