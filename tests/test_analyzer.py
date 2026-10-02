
from src.analyzer import analyze_message


def test_empty_message():
    result = analyze_message("")
    assert result["level"] == "Insufficient input"
    assert result["score"] == 0


def test_guaranteed_returns():
    result = analyze_message(
        "Guaranteed 30% returns in 7 days."
    )
    assert result["score"] == 30
    assert len(result["findings"]) == 1


def test_urgent_pressure():
    result = analyze_message(
        "Act now and send money now."
    )
    assert result["score"] == 20
    assert len(result["findings"]) == 1


def test_sensitive_information_request():
    result = analyze_message(
        "Share your OTP immediately."
    )
    assert result["score"] == 55
    assert len(result["findings"]) == 2


def test_neutral_message():
    result = analyze_message(
        "Read the documents and understand the risks."
    )
    assert result["score"] == 0
    assert len(result["findings"]) == 0
