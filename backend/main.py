from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from tools.time_tool import get_current_time as get_time
from tools.calculator_tool import calculate
from agents.brain import ask_brain
from agents.memory import save_message, load_history, clear_history
from tools.web_search_tool import web_search
from tools.image_tool import generate_image
from tools.file_tool import read_text_file, summarize_file

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hii Bro! NAFRI AI is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/time")
def time():
    return {"answer": get_time()}

@app.get("/agent")
def agent(question: str):
    q = question.lower()
    save_message("user", question)

    if any(word in q for word in ["image", "photo", "picture", "draw", "generate image", "varai"]):
        image_url = generate_image(question)
        result = f"IMAGE::{image_url}::Your image for: {question}"
        save_message("assistant", result)
        return {"answer": result, "image": image_url}

    if any(word in q for word in ["search", "news", "today", "latest", "live", "price", "score", "weather"]):
        result = web_search(question)
        save_message("assistant", result)
        return {"answer": result}

    if "time" in q:
        result = get_time()
        save_message("assistant", result)
        return {"answer": result}

    if "calc" in q or any(op in q for op in ["+", "-", "*", "/"]):
        expr = q.replace("calc", "").strip()
        result = calculate(expr)
        save_message("assistant", result)
        return {"answer": result}

    answer = ask_brain(question)
    save_message("assistant", answer)
    return {"answer": answer}

@app.get("/history")
def history():
    return {"history": load_history()}

@app.get("/clear")
def clear():
    clear_history()
    return {"answer": "History cleared Bro!"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    file_text = read_text_file(content)
    save_message("user", f"Uploaded file: {file.filename}")
    result = summarize_file(file.filename, file_text)
    save_message("assistant", result)
    return {"answer": result, "filename": file.filename, "content": file_text}