# 🛡️ ScamShield AI
### Explainable Financial Scam Warning System

ScamShield AI is an AI-powered financial message analysis tool that combines rule-based warning signals with Machine Learning to identify potentially suspicious messages, highlight evidence, and encourage safer financial decisions.

Built with Python and Streamlit, the project provides an interactive dashboard that helps users understand common warning signs in financial messages.

> **Disclaimer:** ScamShield AI is an educational prototype, not a definitive fraud detector or financial advisor. Its results may be incorrect and should never be treated as proof that a message is fraudulent or legitimate.

## ✨ Key Features

- **Rule-Based Detection:** Identifies predefined warning patterns, including unrealistic return promises, urgent payment requests, and requests for sensitive information.
- **Machine Learning Classification:** Uses TF-IDF text features and Logistic Regression to classify messages as suspicious or not flagged.
- **Explainable Results:** Highlights matched text and explains why a warning signal was detected.
- **Interactive Dashboard:** Provides a dark-themed Streamlit interface for analyzing financial messages.
- **Model Evaluation:** Supports evaluation using precision, recall, F1-score, and a confusion matrix.
- **Safety Guidance:** Encourages independent verification and safer handling of financial information.

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web dashboard |
| Pandas | Dataset loading and processing |
| Scikit-learn | TF-IDF, Logistic Regression, and evaluation |
| Joblib | Saving and loading the trained model |
| Pytest | Automated testing |
| Git & GitHub | Version control and project hosting |

## 🧠 How It Works

1. **Input:** The user enters a financial message into the dashboard.
2. **Rule-Based Analysis:** Predefined text patterns are checked for potential warning signs.
3. **Text Classification:** A trained TF-IDF and Logistic Regression pipeline generates an ML prediction.
4. **Evidence Presentation:** The dashboard displays warning signals, matched text, and explanations.
5. **Safety Guidance:** The user receives general suggestions for independently verifying the message.

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
│   └── train_model.py
└── tests/
    └── test_analyzer.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or newer
- Git

### 1. Clone the repository

```bash
git clone https://github.com/MuhammadSharafat/ScamShield-AI.git
cd ScamShield-AI
```

### 2. Create and activate a virtual environment

**Windows — Git Bash:**

```bash
python -m venv vscam
source vscam/Scripts/activate
```

**Windows — PowerShell:**

```powershell
python -m venv vscam
.\vscam\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model

```bash
python -m src.train_model
```

This creates the trained model at `models/scam_classifier.joblib`.

### 5. Launch the dashboard

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

### 6. Run automated tests

```bash
python -m pytest -v
```

## 📊 Initial Model Evaluation

The initial prototype was trained on a small illustrative dataset containing 20 labelled messages.

| Metric | Initial result |
|---|---:|
| Training examples | 14 |
| Test examples | 6 |
| Test accuracy | 66.7% |
| Suspicious-class precision | 60.0% |
| Suspicious-class recall | 100.0% |
| Suspicious-class F1-score | 75.0% |

**Important:** These preliminary results are based on only six test examples. They are not reliable evidence of real-world detection performance. The dataset needs to be expanded, independently reviewed, and evaluated on representative unseen data before any performance claims can be made.

## 🔐 Privacy and Responsible Use

- Remove names, account numbers, phone numbers, and other personal information before analyzing a message.
- Never share OTPs, passwords, PINs, or private financial credentials.
- Verify suspicious claims using independently obtained official sources.
- Treat both rule-based scores and ML predictions as indicators for further review, not proof of fraud.
- The current implementation processes submitted text in the application; avoid entering sensitive information into any hosted version unless its privacy and logging behavior have been reviewed.

## 🛣️ Future Improvements

- Expand the dataset with diverse, responsibly sourced and reviewed examples.
- Evaluate the model with stronger validation and a representative held-out test set.
- Improve detection of varied wording, context, and previously unseen scam patterns.
- Add more comprehensive automated tests for both the rule-based analyzer and ML pipeline.
- Improve accessibility and mobile responsiveness.
- Deploy the dashboard with appropriate privacy and security safeguards.

## 👨‍💻 Author

**Muhammad Sharafat Alam**

Aspiring Machine Learning Engineer | AI Enthusiast

GitHub: [@MuhammadSharafat](https://github.com/MuhammadSharafat)

---

⭐ If you find this project useful, consider starring the repository.

**Learn. Build. Improve. Repeat.**