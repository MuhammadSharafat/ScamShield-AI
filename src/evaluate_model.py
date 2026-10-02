
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "messages.csv"


def main():
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=["text", "label"])
    df["text"] = df["text"].astype(str).str.strip()
    df = df[df["text"] != ""]

    X = df["text"]
    y = df["label"].astype(int)

    if set(y.unique()) != {0, 1}:
        raise ValueError("Both labels 0 and 1 are required.")

    if y.value_counts().min() < 5:
        raise ValueError(
            "At least 5 examples per class are required "
            "for 5-fold stratified cross-validation."
        )

    model = Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            strip_accents="unicode",
        )),
        ("classifier", LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42,
        )),
    ])

    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42,
    )

    scores = cross_validate(
        model,
        X,
        y,
        cv=cv,
        scoring={
            "accuracy": "accuracy",
            "precision": "precision",
            "recall": "recall",
            "f1": "f1",
        },
        error_score="raise",
    )

    print(f"Dataset size: {len(df)}")
    print("\n5-fold cross-validation results:")

    for metric in ["accuracy", "precision", "recall", "f1"]:
        values = scores[f"test_{metric}"]
        print(
            f"{metric}: "
            f"{values.mean():.3f} ± {values.std():.3f}"
        )

    print(
        "\nWarning: these results are exploratory only. "
        "The dataset is small and illustrative, so they "
        "do not establish real-world scam detection performance."
    )


if __name__ == "__main__":
    main()
