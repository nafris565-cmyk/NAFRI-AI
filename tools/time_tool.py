from datetime import datetime, timezone, timedelta

def get_current_time():
    sri_lanka_time = timezone(timedelta(hours=5, minutes=30))
    now = datetime.now(sri_lanka_time)
    return f"Current time in Sri Lanka is {now.strftime('%I:%M %p, %A, %d %B %Y')}"