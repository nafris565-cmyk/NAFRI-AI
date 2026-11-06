import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key) if api_key else None

MODELS = ["gemini-3.8-flash", "gemini-3.5-flash-lite", "gemini-3-flash"]

from agents.memory import get_context

def ask_brain(question):
    context = get_context()
    full_prompt = f"""You are NAFRI AI, a helpful Premium AI Assistant.
Previous Conversation:
{context}

User new question: {question}
Answer in simple, clear English. Keep it clean without ** or ### symbols."""

    for model_name in MODELS:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=full_prompt
            )
            return response.text
        except Exception as e:
            print(f"Model {model_name} failed: {e}")
            continue
    return "Sorry Bro, Brain is busy now. Try again."