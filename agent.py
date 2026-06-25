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


class ThreatAgent:

    def run(self, text):

        findings = detect_keywords(text)

        return {
            "keywords": findings,
            "count": len(findings)
        }


class EvidenceAgent:

    def run(self, threat_data):

        evidence = []

        for item in threat_data["keywords"]:
            evidence.append(
                f"Suspicious keyword found: {item}"
            )

        return evidence


class RiskAgent:

    def run(self, threat_data):

        score = threat_data["count"] * 20

        score = min(score, 100)

        if score > 80:
            verdict = "Likely Scam"

        elif score > 40:
            verdict = "Suspicious"

        else:
            verdict = "Low Risk"

        return {
            "score": score,
            "verdict": verdict
        }


class SafetyAgent:

    def run(self, verdict):

        if verdict == "Likely Scam":
            return "Do not click links. Block sender."

        if verdict == "Suspicious":
            return "Verify independently."

        return "No major concerns."