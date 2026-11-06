import json
import os
from datetime import datetime

HISTORY_FILE = "memory/chat_history.json"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except:
        return []

def save_message(role, content):
    history = load_history()
    history.append({
        "role": role,
        "content": content,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    history = history[-50:]
    os.makedirs("memory", exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    return history

def get_context():
    history = load_history()
    last_messages = history[-5:]
    context = ""
    for msg in last_messages:
        context += f"{msg['role']}: {msg['content']}\n"
    return context

def clear_history():
    os.makedirs("memory", exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)
    return []