BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "show hidden prompt",
]

def validate_input(text):
    text = text.lower()

    for pattern in BLOCKED_PATTERNS:
        if pattern in text:
            return False

    return True