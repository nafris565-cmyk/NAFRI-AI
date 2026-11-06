import urllib.parse

def generate_image(prompt: str):
    # Real person na, detailed prompt koduppom - AI purinjukkum
    # 【entity-Ronaldo¦canonical_name=ronaldo】 nu sonna, footballer nu serthu solluvom
    low = prompt.lower()
    if "【entity-ronaldo¦canonical_name=ronaldo】" in low:
        prompt = "【entity-Cristiano Ronaldo¦canonical_name=Cristiano Ronaldo】, Portuguese footballer, wearing red 【entity-Manchester United¦canonical_name=Manchester United】 jersey number 7, playing football in stadium, realistic"
    elif "【entity-sachin¦canonical_name=Sachin】" in low:
        prompt = "【entity-Sachin Tendulkar¦canonical_name=Sachin Tendulkar】, Indian cricketer, wearing blue India jersey number 10, holding cricket bat in stadium, realistic"
    elif "cat" in low:
        prompt = "Cute fluffy cat, realistic photo, sitting in garden"
    elif "dog" in low:
        prompt = "Cute happy dog, realistic photo, in park"

    clean_prompt = urllib.parse.quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{clean_prompt}?width=1024&height=1024&seed=42&nologo=true"
    return image_url