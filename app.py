import streamlit as st
from llm import generate_email

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Writing Assistant",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.title("🤖 AI Writing Assistant")
    st.markdown("---")
    st.write("Welcome!")
    st.info(
        """
        This application can:

        ✅ Generate Professional Emails

        ✅ Summarize Long Text

        Powered by Google Gemini
        """
    )

# ----------------------------
# Main Page
# ----------------------------
st.title("✍️ Professional Email Generator")
st.write(
    "Generate professional emails using Artificial Intelligence."
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    recipient = st.text_input(
        "Recipient Name",
        placeholder="John Smith"
    )

    subject = st.text_input(
        "Email Subject",
        placeholder="Project Update"
    )

with col2:
    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Formal",
            "Friendly",
            "Apology",
            "Follow-up",
            "Thank You"
        ]
    )

    length = st.selectbox(
        "Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )

purpose = st.text_area(
    "Purpose of the Email",
    height=180,
    placeholder="Explain why you are writing this email..."
)

if st.button("🚀 Generate Email", use_container_width=True):

    if not recipient or not subject or not purpose:
        st.warning("Please fill all the fields.")
    else:

        with st.spinner("Generating Professional Email..."):

            email = generate_email(
                recipient,
                subject,
                tone,
                length,
                purpose
            )

        st.success("Email Generated Successfully!")

        st.markdown("## 📧 Generated Email")

        st.text_area(
            "Generated Email",
            email,
            height=350
        )