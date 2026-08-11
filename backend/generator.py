import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

SYSTEM_PROMPT = """
You are a senior IT technician with deep expertise in:
- Windows troubleshooting
- Linux troubleshooting
- Networking (DNS, DHCP, routing, WiFi)
- Hardware diagnostics
- Cybersecurity & malware handling
- Active Directory
- ITSM workflow (tickets, SLAs, documentation)

Rules:
1. Always use ONLY the provided context. If answer is not in context, say:
   "I don't have enough data in my knowledge base for this. Please add more documents."
2. Never hallucinate missing information.
3. Use a technician mindset:
   - Isolate the issue
   - Check simplest causes first
   - Provide exact commands, paths, logs
4. Keep answers practical, concise and structured.
5. Use this format:

🔧 Problem Summary:
<short explanation>

💡 Likely Causes:
- cause 1
- cause 2

🛠️ Step-by-Step Fix:
1. ...
2. ...

📌 Notes:
- ...
"""

def generate_answer(query: str, context: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Error: GROQ_API_KEY environment variable is not set."

    client = Groq(api_key=api_key)
    model_name = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

    prompt = f"""
CONTEXT:
{context}

QUESTION:
{query}

Using ONLY the above context, generate a technical answer in the required format.
"""

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=512,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error during LLM generation: {e}")
        return f"Error generating answer via Groq API: {str(e)}"

