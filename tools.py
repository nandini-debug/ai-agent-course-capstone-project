SCAM_WORDS = [
    "winner",
    "lottery",
    "claim now",
    "urgent",
    "reward",
    "click here",
]

def detect_keywords(text):

    findings = []

    for word in SCAM_WORDS:
        if word.lower() in text.lower():
            findings.append(word)

    return findings