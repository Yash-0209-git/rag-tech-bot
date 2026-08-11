import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class QueryExpander:
    def expand(self, query: str) -> str:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return query

        try:
            client = Groq(api_key=api_key)
            model_name = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")
            prompt = f"""
Expand the following short query into a full, meaningful technical question.
Make it detailed but not irrelevant.

Query: "{query}"

Expanded:
"""
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Query expansion failed: {e}")
            return query

