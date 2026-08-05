import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

MODEL = "gemini-3.5-flash"

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 AI Text Summarizer")

st.write(
    "Paste any article, paragraph, report or notes and let AI summarize it."
)

st.markdown("---")

summary_type = st.selectbox(
    "Summary Type",
    [
        "Short",
        "Detailed",
        "Bullet Points",
        "One Line"
    ]
)

text = st.text_area(
    "Paste your text here",
    height=300,
    placeholder="Paste your content..."
)

if st.button("✨ Summarize", use_container_width=True):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        with st.spinner("Generating Summary..."):

            prompt = f"""
Summarize the following text.

Summary Type:
{summary_type}

Text:
{text}
"""

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

        st.success("Summary Generated!")

        st.markdown("## 📄 Summary")

        st.text_area(
            "Generated Summary",
            response.text,
            height=300
        )