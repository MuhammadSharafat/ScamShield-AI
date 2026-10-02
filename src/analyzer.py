
import re


RULES = [
    {
        "name": "Guaranteed or unrealistic returns",
        "patterns": [
            r"\bguaranteed\s+(?:(?:\d{1,3}\s*%\s+)?(?:returns?|profit|income)|(?:\d{1,3}\s*%\s+)?(?:in\s+\d+\s+days?))\b",
            r"\brisk[- ]free\s+(?:returns?|investment)\b",
            r"\bdouble\s+your\s+money\b",
            r"\b\d{1,3}\s*%\s+(?:return|profit)\b",
        ],
        "weight": 30,
        "explanation": (
            "Promises of guaranteed or unusually high returns "
            "can be a warning sign. Verify the claim independently."
        ),
    },
    {
        "name": "Urgent pressure",
        "patterns": [
            r"\bact\s+now\b",
            r"\blimited[- ]time\s+offer\b",
            r"\bonly\s+\d+\s+(?:slots?|hours?)\s+left\b",
            r"\bsend\s+(?:money|payment)\s+now\b",
            r"\bimmediately\b",
        ],
        "weight": 20,
        "explanation": (
            "Pressure to act quickly can discourage careful "
            "verification before sending money."
        ),
    },
    {
        "name": "Requests for sensitive information",
        "patterns": [
            r"\bshare\s+(?:your\s+)?otp\b",
            r"\bsend\s+(?:your\s+)?(?:pin|password)\b",
            r"\benter\s+(?:your\s+)?otp\b",
            r"\bshare\s+(?:your\s+)?bank\s+details\b",
        ],
        "weight": 35,
        "explanation": (
            "Requests to share authentication codes, PINs or "
            "passwords are a serious security warning."
        ),
    },
    {
        "name": "Unverified authority or affiliation",
        "patterns": [
            r"\bofficial\s+sebi\s+approved\b",
            r"\bgovernment\s+approved\s+returns\b",
            r"\bguaranteed\s+by\s+(?:the\s+)?government\b",
        ],
        "weight": 25,
        "explanation": (
            "An authority or regulator name does not prove "
            "that a message or investment is legitimate."
        ),
    },
    {
        "name": "Suspicious payment language",
        "patterns": [
            r"\bpay\s+(?:a\s+)?registration\s+fee\b",
            r"\bpay\s+(?:a\s+)?withdrawal\s+fee\b",
            r"\btransfer\s+to\s+(?:my|this)\s+personal\s+account\b",
        ],
        "weight": 25,
        "explanation": (
            "Unexpected fees or requests to transfer funds to "
            "a personal account should be independently verified."
        ),
    },
]


def analyze_message(message: str) -> dict:
    """Find explainable warning signals in a financial message."""

    text = re.sub(r"\s+", " ", message).strip()

    if not text:
        return {
            "score": 0,
            "level": "Insufficient input",
            "findings": [],
            "summary": "Enter a message to analyze.",
        }

    findings = []
    total_score = 0

    for rule in RULES:
        matched = []

        for pattern in rule["patterns"]:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                phrase = match.group(0)
                if phrase.lower() not in [
                    item.lower() for item in matched
                ]:
                    matched.append(phrase)

        if matched:
            total_score += rule["weight"]
            findings.append({
                "name": rule["name"],
                "evidence": matched,
                "explanation": rule["explanation"],
                "points": rule["weight"],
            })

    score = min(total_score, 100)

    if score >= 60:
        level = "High"
        summary = (
            "Multiple or serious warning signals were detected. "
            "Do not send money or sensitive information before "
            "independent verification."
        )
    elif score >= 30:
        level = "Moderate"
        summary = (
            "Potential warning signals were detected. "
            "Verify the claims and sender independently."
        )
    elif score > 0:
        level = "Some warning signs"
        summary = (
            "A warning signal was detected. This alone does not "
            "establish that the message is fraudulent."
        )
    else:
        level = "No obvious signals detected"
        summary = (
            "These rules did not detect a known warning pattern. "
            "This does not mean the message is safe or legitimate."
        )

    return {
        "score": score,
        "level": level,
        "findings": findings,
        "summary": summary,
    }
