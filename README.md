# 🤖 AI Writing Assistant

An AI-powered web application that helps users generate professional emails and summarize lengthy text using Google's Gemini Large Language Model (LLM). The application is built with **Python**, **Streamlit**, and the **Google GenAI SDK**, providing an intuitive interface for AI-assisted writing.

---

## 📌 Features

### 📧 Professional Email Generator
- Generate professional emails based on user requirements.
- Select different tones (Formal, Friendly, Professional, etc.).
- Choose the desired email length.
- AI-generated subject-focused content.

### 📝 AI Text Summarizer
- Summarize long paragraphs into concise summaries.
- Select summary length.
- Maintain key information while reducing text size.

### 🔒 Secure API Management
- Environment variables for local development.
- Streamlit Secrets for cloud deployment.

### ☁️ Cloud Deployment
- Deployed using Streamlit Community Cloud.
- Source code hosted on GitHub.

---

# 🏗️ Project Architecture

```
                    User
                      │
                      ▼
            Streamlit Web Interface
                      │
                      ▼
              User Input Prompt
                      │
                      ▼
             Prompt Engineering
                      │
                      ▼
         Google Gemini Large Language Model
                      │
                      ▼
             AI Generated Response
                      │
                      ▼
              Display Result
```

---

# 📂 Project Structure

```
AI-Writing-Assistant/

│── app.py
│── llm.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env
│
├── pages/
│     └── Text_Summarizer.py
│
├── assets/
│
└── venv/
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend Development |
| Streamlit | Web Application Framework |
| Google Gemini | Large Language Model |
| Google GenAI SDK | AI Integration |
| python-dotenv | Environment Variable Management |
| Git | Version Control |
| GitHub | Source Code Hosting |
| Streamlit Community Cloud | Deployment |

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Writing-Assistant.git
```

## Navigate to Project

```bash
cd AI-Writing-Assistant
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

> **Note:** Never commit your `.env` file to GitHub.

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

# ☁️ Deployment

This project is deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new app.
4. Select the GitHub repository.
5. Set `app.py` as the main file.
6. Add the following secret:

```toml
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

7. Deploy the application.

---

# 📖 How It Works

## Professional Email Generator

1. Enter the recipient.
2. Enter the subject.
3. Describe the purpose.
4. Select email tone.
5. Select email length.
6. Click **Generate Email**.
7. Gemini AI creates a professional email.

---

## Text Summarizer

1. Paste the text.
2. Select summary length.
3. Click **Summarize**.
4. Gemini AI generates a concise summary.

---

# ✨ Features

- Professional Email Generation
- AI Text Summarization
- Responsive Streamlit Interface
- Google Gemini Integration
- Prompt Engineering
- Secure API Key Management
- Cloud Deployment
- Beginner-Friendly Design

---

# 📈 Future Enhancements

- PDF Export
- Word Document Export
- Copy to Clipboard
- Email Templates
- Chat History
- Multi-language Support
- Grammar Checker
- Dark Mode
- User Authentication
- AI Resume Generator
- AI Cover Letter Generator

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Python Programming
- Streamlit Development
- Prompt Engineering
- Google Gemini API Integration
- Environment Variables
- Git & GitHub
- Cloud Deployment
- Large Language Models (LLMs)
- AI-powered Application Development

---

# ⚠️ Limitations

- Requires an active internet connection.
- Depends on Google Gemini API availability.
- API usage limits may apply.
- Large inputs may increase response time.

---

# 👨‍💻 Author

**Nishaa Subramaniam**

B.Tech Information Technology

AI & Full Stack Developer

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://www.linkedin.com/in/YOUR_PROFILE

---

# 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Your support is appreciated!
