import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

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