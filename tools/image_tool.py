import urllib.parse

def generate_image(prompt: str):
    # Free Image Generation - No API Key needed
    clean_prompt = urllib.parse.quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=1024&height=1024&seed=42&nologo=true"
    return image_url