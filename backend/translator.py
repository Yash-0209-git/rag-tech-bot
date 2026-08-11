import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def translate_to_english(text):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return text
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": f"Translate this to English:\n{text}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Translation error: {e}")
        return text


def translate_from_english(text, target_language):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return text
    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": f"Translate this to {target_language}:\n{text}"}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Translation error: {e}")
        return text


def detect_language(text):
    if any(ch in text for ch in "அஆஇஈஉஊஎஏஐஒஓஔஃஂ"):
        return "Tamil"
    if any(ch in text for ch in "अआइईउऊएऐओऔ"):
        return "Hindi"
    return "English"

