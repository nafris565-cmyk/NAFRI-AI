from google import genai
import os
import time
from dotenv import load_dotenv
from agents.memory import get_context

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3-flash",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash"
]

def ask_brain(question):
    context = get_context()
    full_prompt = f"Previous: {context}\nUser: {question}\nAnswer in simple, clear English. Keep short and clean without ** or ### symbols."

    for model_name in MODELS:
        try:
            print(f"Trying model: {model_name}")
            response = client.models.generate_content(
                model=model_name,
                contents=full_prompt
            )
            if response.text:
                return response.text
        except Exception as e:
            print(f"Model {model_name} failed: {e}")
            time.sleep(1)
            continue
    return "Google Server is busy now (503). Please wait 30 seconds and try again."