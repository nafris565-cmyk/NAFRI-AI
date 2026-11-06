def read_text_file(content: bytes):
    try:
        text = content.decode("utf-8", errors="ignore")
        # First 3000 characters mattum Brain-kku anuppuvom
        if len(text) > 3000:
            text = text[:3000] + "\n... [File too big, first part only]"
        return text
    except Exception as e:
        return f"File read failed: {e}"

def summarize_file(filename: str, file_text: str):
    return f"File '{filename}' uploaded successfully.\n\nContent preview:\n{file_text}\n\n---\nNow you can ask: 'Summarize this file' or 'What is in this file?'"