
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "messages.csv"


def validate_dataset():
    df = pd.read_csv(DATA_PATH)

    required_columns = {"text", "label"}

    if not required_columns.issubset(df.columns):
        raise ValueError(
            "Dataset must contain 'text' and 'label' columns."
        )

    df["text"] = df["text"].fillna("").astype(str).str.strip()

    if df["text"].eq("").any():
        raise ValueError("Dataset contains empty messages.")

    if df["label"].isna().any():
        raise ValueError("Dataset contains missing labels.")

    labels = set(df["label"].unique())

    if not labels.issubset({0, 1}):
        raise ValueError("Labels must be 0 or 1.")

    duplicates = df["text"].duplicated().sum()

    print(f"Total messages: {len(df)}")
    print(f"Label counts:\n{df['label'].value_counts().sort_index()}")
    print(f"Duplicate messages: {duplicates}")

    if duplicates:
        print(
            "Warning: review duplicate messages before training. "
            "Do not automatically remove them without checking labels."
        )

    print("Dataset validation completed.")


if __name__ == "__main__":
    validate_dataset()
