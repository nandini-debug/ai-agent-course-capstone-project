class KeywordSkill:

    def analyze(self, text):

        keywords = [
            "winner",
            "lottery",
            "urgent",
            "reward",
            "claim now",
            "click here"
        ]

        found = []

        for word in keywords:
            if word.lower() in text.lower():
                found.append(word)

        return found


class RiskScoreSkill:

    def calculate(self, count):

        return min(count * 20, 100)


def detect_scam_type(text):

    text = text.lower()

    if (
        "job" in text or
        "registration fee" in text or
        "work from home" in text or
        "no interview" in text
    ):
        return "Fake Job Scam"

    if (
        "upi" in text or
        "payment" in text or
        "collect request" in text or
        "refund" in text
    ):
        return "UPI Scam"

    if (
        "click here" in text or
        "verify account" in text or
        "suspended account" in text
    ):
        return "Phishing Scam"

    if (
        "whatsapp" in text or
        "account blocked" in text
    ):
        return "WhatsApp Scam"

    if (
        "winner" in text or
        "lottery" in text
    ):
        return "Lottery Scam"

    return "Unknown"