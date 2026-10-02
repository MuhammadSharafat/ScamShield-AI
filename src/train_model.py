
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "messages.csv"
MODEL_DIR = ROOT / "models"
MODEL_PATH = MODEL_DIR / "scam_classifier.joblib"


def main():
    df = pd.read_csv(DATA_PATH)

    if not {"text", "label"}.issubset(df.columns):
        raise ValueError("CSV must contain text and label columns.")

    df = df.dropna(subset=["text", "label"])
    df["text"] = df["text"].astype(str).str.strip()
    df = df[df["text"] != ""]

    if set(df["label"].unique()) != {0, 1}:
        raise ValueError("Dataset must contain both labels 0 and 1.")

    if df["label"].value_counts().min() < 4:
        raise ValueError("Need at least 4 examples per class.")

    X_train, X_test, y_train, y_test = train_test_split(
        df["text"],
        df["label"].astype(int),
        test_size=0.30,
        random_state=42,
        stratify=df["label"],
    )

    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2),
                strip_accents="unicode",
            ),
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42,
            ),
        ),
    ])

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"Dataset size: {len(df)}")
    print(f"Training examples: {len(X_train)}")
    print(f"Test examples: {len(X_test)}")
    print("\nClassification report:")
    print(
        classification_report(
            y_test,
            predictions,
            labels=[0, 1],
            target_names=[
                "Not labelled suspicious",
                "Suspicious",
            ],
            zero_division=0,
        )
    )

    print("Confusion matrix (rows=true, columns=predicted):")
    print(confusion_matrix(y_test, predictions, labels=[0, 1]))

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"\nModel saved to: {MODEL_PATH}")


if __name__ == "__main__":
    main()
