import os
from dotenv import load_dotenv
import streamlit as st
from google import genai

load_dotenv()

# Read API key from Streamlit Secrets first, then .env
api_key = st.secrets.get("GOOGLE_API_KEY", os.getenv("GOOGLE_API_KEY"))

if not api_key:
    raise ValueError("GOOGLE_API_KEY is missing.")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash"


def generate_email(recipient, subject, tone, length, purpose):

    prompt = f"""
You are a professional email writer.

Write a {tone} email.

Recipient:
{recipient}

Subject:
{subject}

Purpose:
{purpose}

Length:
{length}

Generate only the email.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return response.text