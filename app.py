
import streamlit as st

from src.analyzer import analyze_message
from src.predictor import predict_message


st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide",
)

st.markdown("""
<style>
.stApp {
    background: #0b1120;
    color: #edf2f7;
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}
.hero {
    padding: 1.5rem;
    border: 1px solid #263449;
    border-radius: 18px;
    background: linear-gradient(120deg, #111d32, #122b35);
    margin-bottom: 1.5rem;
}
.small-note {
    color: #a8b8ca;
    font-size: 0.9rem;
}
.result-card {
    padding: 1rem;
    border: 1px solid #304158;
    border-radius: 12px;
    margin: 0.5rem 0 1rem 0;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>🛡️ ScamShield AI</h1>
    <p>Understand suspicious financial messages before you act.</p>
    <p class="small-note">
        Explainable warning signals · Machine Learning · Evidence-first analysis
    </p>
</div>
""", unsafe_allow_html=True)


with st.sidebar:
    st.header("About ScamShield")
    st.write(
        "Analyze financial messages using predefined warning "
        "patterns and a prototype text-classification model."
    )
    st.divider()
    st.caption("Prototype v0.2")
    st.caption("Educational tool — not proof of fraud.")


st.subheader("Analyze a financial message")

samples = {
    "Choose a demo message": "",
    "Guaranteed returns": (
        "Guaranteed 30% returns in 7 days. "
        "Act now and send money now to reserve your slot!"
    ),
    "Sensitive information request": (
        "Your account will be blocked. "
        "Share your OTP immediately to keep it active."
    ),
    "Neutral example": (
        "Learn about financial risks and diversification. "
        "Read the scheme documents before investing."
    ),
}

selected = st.selectbox("Try a sample", list(samples.keys()))

message = st.text_area(
    "Paste the message here",
    value=samples[selected],
    height=170,
    max_chars=10000,
    placeholder="Remove personal details before submitting.",
)

if st.button(
    "🔎 Analyze message",
    type="primary",
    use_container_width=True,
):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        rules = analyze_message(message)

        try:
            ml = predict_message(message)
        except (FileNotFoundError, ValueError, OSError) as exc:
            st.error(f"ML model could not run: {exc}")
            st.stop()

        st.divider()
        st.subheader("Analysis report")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Rule-based warning score",
                f"{rules['score']}/100",
            )
            st.caption("Heuristic score, not a probability.")

        with col2:
            st.metric(
                "Warning patterns found",
                len(rules["findings"]),
            )

        st.info(f"Rule-based result: {rules['level']}")
        st.write(rules["summary"])

        st.subheader("Machine Learning result")

        if ml["label"] == 1:
            st.warning("ML model: Suspicious message")
        else:
            st.info("ML model: Not flagged as suspicious")

        st.metric(
            "Model suspicious-class score",
            f"{ml['probability']}%",
        )

        st.caption(
            "This is the model's estimated class probability, "
            "not a calibrated real-world scam probability. "
            "The model was trained on a tiny demo dataset."
        )

        st.subheader("Rule-based evidence")

        if rules["findings"]:
            for item in rules["findings"]:
                with st.expander(item["name"], expanded=True):
                    st.write(item["explanation"])
                    st.write("Matched text:")
                    for phrase in item["evidence"]:
                        st.code(phrase)
        else:
            st.info(
                "No patterns from the current rule set matched. "
                "Other warning signs may still be present."
            )

        st.subheader("Safer next steps")
        st.markdown("""
        - Verify the sender through an independently found official channel.
        - Never share OTPs, PINs or passwords.
        - Do not transfer money under pressure.
        - Verify financial claims with relevant official sources.
        """)

        with st.expander("Methodology and limitations"):
            st.write(
                "The rule-based score adds predefined weights for "
                "matched patterns. The ML component uses TF-IDF and "
                "Logistic Regression trained on a small, illustrative "
                "dataset. Neither result proves fraud or safety."
            )
            st.write(
                "The current dataset contains only 20 messages, "
                "so the ML prediction may be unreliable and may "
                "not generalize to real messages."
            )
            st.write(
                "Avoid entering personal, account, payment or "
                "authentication details."
            )


st.divider()
st.caption(
    "ScamShield AI is an educational safety prototype. "
    "It does not certify investments or establish fraud."
)
