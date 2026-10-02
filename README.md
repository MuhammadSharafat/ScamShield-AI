# 🛡️ ScamShield AI
### Explainable Financial Scam Warning System

ScamShield AI is an AI-powered financial message analysis tool that combines rule-based warning signals with Machine Learning to identify potentially suspicious messages, highlight evidence, and encourage safer financial decisions.

Built with Python and Streamlit, this project provides an interactive dashboard that helps users understand common warning signs in financial messages.

## 🚀 Live Demo

**Try ScamShield AI:** [Open Live Application](https://scamshield-ai-fyfhkxe4779egmd9tsvuhq.streamlit.app/)

Explore the interactive dashboard and review the warning signals detected in financial messages.

> **Disclaimer:** ScamShield AI is an educational prototype, not a definitive fraud detector or financial advisor. Its results may be incorrect and should never be treated as proof that a message is fraudulent or legitimate.

## ✨ Key Features

- 🔍 **Rule-Based Detection:** Identifies predefined warning patterns, including unrealistic return promises, urgent payment requests, and requests for sensitive information.
- 🤖 **Machine Learning Classification:** Uses TF-IDF text features and Logistic Regression to classify messages as suspicious or not flagged.
- 🔎 **Explainable Results:** Highlights matched text and explains why a warning signal was detected.
- 📊 **Interactive Dashboard:** Provides a dark-themed Streamlit interface for analyzing financial messages.
- 🧪 **Model Evaluation:** Includes accuracy, precision, recall, F1-score, confusion matrix, and cross-validation tools.
- ✅ **Dataset Validation:** Checks dataset labels, empty messages, and duplicate entries.
- 🔐 **Safety Guidance:** Encourages independent verification and safer handling of financial information.

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web dashboard |
| Pandas | Dataset loading and processing |
| Scikit-learn | TF-IDF, Logistic Regression, and model evaluation |
| Joblib | Saving and loading the trained model |
| Pytest | Automated testing |
| Git & GitHub | Version control and project hosting |

## 🧠 How It Works

1. **Input:** The user enters a financial message into the dashboard.
2. **Rule-Based Analysis:** Predefined text patterns are checked for potential warning signs.
3. **Text Classification:** A trained TF-IDF and Logistic Regression pipeline generates a machine learning prediction.
4. **Evidence Presentation:** The dashboard displays detected warning signals, matched text, and explanations.
5. **Safety Guidance:** The user receives general suggestions for independently verifying suspicious claims.

## 🏗️ Project Structure

```text
ScamShield-AI/
├── app.py
├── requirements.txt
├── .gitignore
├── data/
│   └── messages.csv
├── models/
│   └── scam_classifier.joblib
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── predictor.py
│   ├── train_model.py
│   ├── validate_dataset.py
│   └── evaluate_model.py
└── tests/
    └── test_analyzer.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or newer
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/MuhammadSharafat/ScamShield-AI.git
cd ScamShield-AI
```

### 2. Create and Activate a Virtual Environment

**Windows — Git Bash**

```bash
python -m venv vscam
source vscam/Scripts/activate
```

**Windows — PowerShell**

```powershell
python -m venv vscam
.\vscam\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Validate the Dataset

```bash
python -m src.validate_dataset
```

This checks the dataset structure, label distribution, empty messages, and duplicate entries.

### 5. Train the Machine Learning Model

```bash
python -m src.train_model
```

This trains the TF-IDF and Logistic Regression pipeline and saves the model to `models/scam_classifier.joblib`.

### 6. Run Model Evaluation

```bash
python -m src.evaluate_model
```

This script evaluates the model using stratified cross-validation and reports accuracy, precision, recall, and F1-score.

### 7. Launch the Dashboard

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

### 8. Run Automated Tests

```bash
python -m pytest -v
```

## 📊 Model Evaluation

The current prototype uses a small dataset of **30 illustrative synthetic messages**, with 15 examples in each class.

A preliminary holdout evaluation used 21 training examples and 9 test examples. The observed test accuracy was 88.9%.

A separate five-fold cross-validation run produced the following exploratory results:

| Metric | Mean | Standard Deviation |
|---|---:|---:|
| Accuracy | 86.7% | 19.4 percentage points |
| Precision | 85.0% | 20.0 percentage points |
| Recall | 93.3% | 13.3 percentage points |
| F1-score | 88.6% | 16.7 percentage points |

These results are **exploratory, not evidence of reliable real-world scam detection**. The dataset is small and synthetic, so results may vary substantially with different samples. A larger, independently reviewed dataset and representative unseen test data are needed for meaningful real-world evaluation.

The model's class score is not a calibrated probability that a message is a scam.

## 🧪 Testing and Data Validation

The project includes automated tests for selected rule-based warning patterns and a dataset validation script.

Run the tests with:

```bash
python -m pytest -v
```

Validate the dataset with:

```bash
python -m src.validate_dataset
```

Evaluate the model with:

```bash
python -m src.evaluate_model
```

## 🔐 Privacy and Responsible Use

- Remove names, account numbers, phone numbers, and other personal information before analyzing a message.
- Never share OTPs, passwords, PINs, or private financial credentials.
- Verify suspicious claims using independently obtained official sources.
- Treat rule-based scores and machine learning predictions as indicators for further review, not proof of fraud.
- Avoid entering sensitive information into the hosted application unless its privacy and logging behavior have been reviewed.

## 🛣️ Future Improvements

- Expand the dataset with diverse, responsibly sourced and reviewed examples.
- Evaluate the model using representative, independently collected test data.
- Improve detection of varied wording, context, and previously unseen scam patterns.
- Add comprehensive automated tests for both the rule-based analyzer and machine learning pipeline.
- Improve accessibility and mobile responsiveness.
- Strengthen privacy safeguards and deployment practices.

## 👨‍💻 Author

**Muhammad Sharafat Alam**

Aspiring Machine Learning Engineer | AI Enthusiast

- GitHub: [@MuhammadSharafat](https://github.com/MuhammadSharafat)
- Live Demo: [ScamShield AI](https://scamshield-ai-fyfhkxe4779egmd9tsvuhq.streamlit.app/)

---

⭐ If you find this project useful, consider starring the repository.

**Learn. Build. Improve. Repeat.**
