import datetime

# ---- Helper Functions ----
def to_upper(text: str) -> str:
    return text.upper()

def to_lower(text: str) -> str:
    return text.lower()

def strip_spaces(text: str) -> str:
    return text.strip()

def replace_text(text: str, old: str, new: str) -> str:
    return text.replace(old, new)

def count_substring(text: str, substring: str) -> int:
    return text.count(substring)

def get_text_stats(text: str):
    lines = text.splitlines()
    words = text.split()
    return {
        "line_count": len(lines),
        "word_count": len(words),
        "char_count": len(text)
    }

def append_text(original_text: str, extra_text: str) -> str:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{original_text}\n{extra_text}\n\nProcessed on: {timestamp}"
