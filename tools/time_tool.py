from datetime import datetime, timezone, timedelta

def get_current_time():
    tz = timezone(timedelta(hours=5, minutes=30))
    now = datetime.now(tz)
    return {
        "time": now.strftime("%I:%M %p"),
        "date": now.strftime("%A, %d %B %Y"),
        "timezone": "Asia/Colombo"
    }