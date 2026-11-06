try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS

def web_search(query: str):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            if not results:
                return "Sorry Bro, Internet-la onnum kedaikkala."
            
            answer = f"Live Search Results for '{query}':\n\n"
            for i, r in enumerate(results, 1):
                answer += f"{i}. {r['title']}\n"
                answer += f"{r['body']}\n"
                answer += f"Link: {r['href']}\n\n"
            return answer
    except Exception as e:
        return f"Search failed Bro: {e}"