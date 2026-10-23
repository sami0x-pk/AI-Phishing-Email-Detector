# 🛡️ AI Phishing Email Detector

### Machine Learning-Based Email Threat Analysis

An educational cybersecurity application that uses Machine Learning and rule-based analysis to identify potential phishing indicators in email text. Built with Python and Streamlit, the project provides an interactive dashboard for analyzing suspicious email content and understanding common phishing warning signs.

## 🚀 Features

- **AI-Based Classification:** Classifies email text as potentially phishing or legitimate.
- **Threat Indicator Analysis:** Identifies suspicious keywords and phrases.
- **URL Extraction:** Detects URLs present in email content.
- **Threat Indicator Score:** Displays a heuristic score based on detected warning signs.
- **Security Recommendations:** Provides practical advice for safer email handling.
- **Interactive Dashboard:** User-friendly interface built with Streamlit.
- **Machine Learning Notebook:** Includes a Jupyter Notebook for exploring data, training the model, and evaluating its performance.

## 🧰 Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Jupyter Notebook

## 📂 Project Structure

```text
AI-Phishing-Email-Detector/
│
├── app.py
├── AI_Phishing_Email_Detector.ipynb
├── requirements.txt
├── README.md
└── Run Dashboard.bat
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Phishing-Email-Detector.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Directory

```bash
cd AI-Phishing-Email-Detector
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the dashboard.

## 🧪 How to Use

1. Launch the application.
2. Paste the email subject and message into the text area.
3. Click **ANALYZE EMAIL**.
4. Review the model's classification.
5. Examine detected threat indicators and extracted URLs.
6. Follow the security recommendations.

## 🧠 Machine Learning Approach

The prototype uses a Scikit-learn pipeline consisting of:

- **TF-IDF Vectorizer:** Converts email text into numerical features.
- **Logistic Regression:** Classifies the email using the learned text features.

The current demonstration dataset is small and manually created. Its predictions and evaluation results should not be interpreted as evidence of real-world detection performance.

## ⚠️ Limitations

This project is an educational prototype, not a production-grade security solution.

- The model uses a very small sample dataset.
- Predictions may be inaccurate for unfamiliar email patterns.
- The threat indicator score is heuristic-based and is not a calibrated probability.
- URLs are extracted but are not checked against live threat intelligence.
- Email headers, sender authentication, and attachments are not analyzed.
- A legitimate prediction does not guarantee that an email is safe.

Always verify suspicious messages through an independent, trusted communication channel.

## 🔮 Future Improvements

- Train and evaluate the model on a larger, representative labelled dataset.
- Add precision, recall, F1-score, and confusion matrix reporting.
- Improve phishing URL analysis using reputable threat intelligence sources.
- Add email header and authentication-result analysis.
- Implement scan history and downloadable reports.
- Improve the dashboard with analytics and visualizations.

## 🎯 Project Objective

To demonstrate how Machine Learning and basic cybersecurity rules can help users recognize common phishing indicators and improve email security awareness.

## 👨‍💻 Project Type

Educational project — Machine Learning and Cybersecurity Awareness.

---

**Disclaimer:** This application is intended for educational and awareness purposes only. It must not be used as the sole basis for deciding whether an email is safe.
