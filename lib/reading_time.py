def estimate_reading_time(text):
    word_count = len(text.split())
    estimate = int(word_count / 200)
    return f"{estimate} minute"
