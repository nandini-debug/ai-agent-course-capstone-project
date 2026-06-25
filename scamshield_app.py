import streamlit as st

from workflow import InvestigationFlow
from security import validate_input

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
# 🛡️ ScamShield AI

### Multi-Agent Digital Trust Investigator

Detect:
- 💼 Fake Job Scams
- 💳 UPI Payment Scams
- 🎣 Phishing Attacks
- 📱 WhatsApp Scams

Built using:
- Multi-Agent Architecture
- Agent Skills
- Security Layer
""")

with st.sidebar:

    st.header(" ScamShield Architecture")

    st.markdown("""
###  User Message

⬇️

### 🕵️ Threat Agent
Keyword Detection

⬇️

### 📄 Evidence Agent
Evidence Collection

⬇️

### 📊 Risk Agent
Risk Scoring

⬇️

### 🛡️ Safety Agent
Safety Recommendation

⬇️

###  Final Scam Report
""")

    st.divider()

    st.subheader("Implemented Concepts")

    st.success(" Multi-Agent System")
    st.success(" Agent Skills")
    st.success(" Security Layer")

    st.divider()

    st.subheader("Supported Scam Types")

    st.info("💼 Fake Job Scam")
    st.info("💳 UPI Payment Scam")
    st.info(" Phishing Scam")
    st.info("📱 WhatsApp Scam")

    st.divider()

    st.subheader("Project")

    st.write(
        "ScamShield AI - Multi-Agent Digital Trust Investigator"
    )

message = st.text_area(
    "Paste suspicious message"
)

if st.button("Analyze"):

    if not validate_input(message):

        st.error(
            "Prompt blocked by security."
        )

        st.stop()

    result = InvestigationFlow().execute(
        message
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Risk Score",
            result["risk"]["score"]
        )

    with col2:
        st.metric(
            "Indicators",
            result["threat"]["count"]
        )

    with col3:
        st.metric(
            "Verdict",
            result["risk"]["verdict"]
        )

    with col4:
        st.metric(
            "Scam Type",
            result["scam_type"]
        )

    st.progress(
        result["risk"]["score"] / 100
    )

    st.subheader("🤖 Agent Execution Timeline")

    st.success("ThreatAgent Executed")
    st.success("EvidenceAgent Executed")
    st.success("RiskAgent Executed")
    st.success("SafetyAgent Executed")
    
    st.subheader("🔗 URL Analysis")

    if result["urls"]:
        for url in result["urls"]:
            st.warning(url)
    else:
        st.success("No URLs detected")

    st.subheader("📄 Evidence Report")

    for item in result["evidence"]:
        st.write("•", item)

    st.subheader("🔍 Detected Indicators")

    for item in result["threat"]["keywords"]:
        st.info(item)

    st.subheader("🛡️ Recommendation")

    st.success(
        result["advice"]
    )