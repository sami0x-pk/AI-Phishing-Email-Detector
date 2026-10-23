
import re
import streamlit as st

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

st.set_page_config(
    page_title="AI Phishing Email Detector",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #07111f;
    color: #e6edf7;
}
[data-testid="stSidebar"] {
    background-color: #0d1b2a;
}
h1, h2, h3 {
    color: #00e5ff !important;
}
.stButton > button {
    background-color: #00bcd4;
    color: #06111c;
    font-weight: bold;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Small educational dataset
emails = [
    "Urgent verify your bank account immediately",
    "You won a lottery claim your free prize",
    "Your account is suspended confirm your password",
    "Click this link to claim your reward",
    "Update your banking details immediately",
    "Your password expires today verify your account",
    "Your university lecture starts tomorrow at 9 AM",
    "Please find the assignment attached to this email",
    "Our meeting is scheduled for Monday",
    "Your project report has been received",
    "Thank you for attending today's class",
    "The examination timetable is available",
    "Please review the document before the meeting",
    "Your library book is due tomorrow"
]

labels = [
    "Phishing", "Phishing", "Phishing", "Phishing",
    "Phishing", "Phishing", "Legitimate", "Legitimate",
    "Legitimate", "Legitimate", "Legitimate", "Legitimate",
    "Legitimate", "Legitimate"
]

@st.cache_resource
def load_model():
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("classifier", LogisticRegression(max_iter=1000))
    ])
    pipeline.fit(emails, labels)
    return pipeline

model = load_model()

patterns = {
    "Urgency": r"\b(urgent|immediately|act now|expires today)\b",
    "Credential request": r"\b(password|verify your account|login details)\b",
    "Financial request": r"\b(bank account|banking details|send money)\b",
    "Prize or reward": r"\b(lottery|free prize|claim your reward)\b",
    "Suspicious link language": r"\b(click here|click this link)\b"
}

st.sidebar.title("🛡️ PHISHGUARD AI")
st.sidebar.caption("Cybersecurity Analysis Dashboard")
st.sidebar.divider()
st.sidebar.write("📧 Email Analysis")
st.sidebar.write("🚨 Threat Indicators")
st.sidebar.write("🌐 URL Extraction")
st.sidebar.write("🛡️ Security Recommendations")
st.sidebar.divider()
st.sidebar.caption("Educational prototype")

st.title("🛡️ AI Phishing Email Detector")
st.write("Machine learning + rule-based email threat analysis.")

st.warning(
    "Prototype warning: This model uses a tiny sample dataset. "
    "Its predictions are experimental and cannot establish email safety."
)

c1, c2, c3 = st.columns(3)
c1.metric("Detection Engine", "ML + Rules")
c2.metric("Indicator Types", len(patterns))
c3.metric("Analysis Mode", "Email Text")

st.divider()

email_text = st.text_area(
    "📧 Paste email text",
    height=200,
    placeholder="Paste the email subject and message here..."
)

if st.button("🔍 ANALYZE EMAIL", use_container_width=True):

    if not email_text.strip():
        st.warning("Please paste an email first.")

    else:
        prediction = model.predict([email_text])[0]
        indicators = []

        for name, pattern in patterns.items():
            if re.search(pattern, email_text, re.IGNORECASE):
                indicators.append(name)

        urls = re.findall(
            r"https?://[^\s]+|www\.[^\s]+",
            email_text,
            re.IGNORECASE
        )

        if urls:
            indicators.append("URL Found")

        score = min(len(indicators) * 20, 100)

        if indicators and prediction == "Legitimate":
            status = "Needs Manual Review"
        else:
            status = prediction

        st.divider()
        st.subheader("📊 Analysis Results")

        a, b = st.columns(2)
        a.metric("Threat Indicator Score", f"{score}/100")
        b.metric("Indicators Found", len(indicators))

        st.progress(score / 100)

        if status == "Phishing":
            st.error("🚨 AI Prediction: Potential Phishing")
        elif status == "Needs Manual Review":
            st.warning("⚠️ Result: Needs Manual Review")
        else:
            st.success("AI Prediction: Likely Legitimate")

        st.caption(
            "Threat score counts matching indicators; it is not a "
            "probability of maliciousness."
        )

        st.subheader("🔎 Suspicious Indicators")
        if indicators:
            for item in indicators:
                st.write("⚠️", item)
        else:
            st.write("No configured warning patterns were detected.")

        st.subheader("🌐 URLs Found")
        if urls:
            for url in urls:
                st.code(url)
            st.warning(
                "URL destinations have not been checked. "
                "Do not open suspicious links."
            )
        else:
            st.write("No URL pattern detected.")

        st.subheader("🛡️ Security Recommendations")
        for advice in [
            "Never share passwords or OTPs through email links.",
            "Verify urgent requests through an independent official channel.",
            "Check the sender's full email address and domain.",
            "Avoid unexpected links and attachments."
        ]:
            st.write("•", advice)

        st.caption(
            "This educational tool does not inspect email headers, "
            "attachments, sender authentication or live URL reputation. "
            "A legitimate prediction does not guarantee safety."
        )

st.divider()
st.caption("AI Phishing Email Detector | Cybersecurity Awareness Project")
