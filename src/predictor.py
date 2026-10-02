
from pathlib import Path

import joblib


ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "scam_classifier.joblib"

_model = None


def predict_message(message: str) -> dict:
    global _model

    if not message or not message.strip():
        return {
            "label": None,
            "probability": None,
            "message": "Enter a message to analyze.",
        }

    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                "Model not found. Run: python -m src.train_model"
            )
        _model = joblib.load(MODEL_PATH)

    prediction = int(_model.predict([message])[0])
    probabilities = _model.predict_proba([message])[0]
    classes = list(_model.classes_)
    suspicious_probability = float(
        probabilities[classes.index(1)]
    )

    return {
        "label": prediction,
        "probability": round(suspicious_probability * 100, 1),
        "message": (
            "Model flags this message as suspicious."
            if prediction == 1
            else "Model did not flag this message as suspicious."
        ),
    }
