from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

models = client.models.list()

print("=== AVAILABLE GROQ MODELS ===")
for m in models.data:
    print("-", m.id)
