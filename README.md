# 🤖 AI Resume Assistant

An AI-powered Resume Chatbot built using **Streamlit** and **Google Gemini API**. The application acts as a virtual resume assistant that answers questions about my education, skills, projects, certifications, and experience. If a question is unrelated to my resume, it responds using general knowledge.

---

## 🚀 Features

- 📄 Interactive AI Resume Assistant
- 💬 Chat-based interface using Streamlit
- 🤖 Powered by Google Gemini 2.5 Flash
- 📝 Answers questions based on my resume
- 🌍 Can also answer general knowledge questions
- 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- python-dotenv

---

## 📂 Project Structure

```
resume-bot/
│
├── resume_bot.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/resume-bot.git

cd resume-bot
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Gemini API

Create a `.env` file in the project directory.

```env
GOOGLE_GEMINI_KEY=YOUR_API_KEY
```

Get your API key from **Google AI Studio**.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 💡 Example Questions

You can ask questions like:

- Tell me about Prachi.
- What programming languages does she know?
- What are her projects?
- Explain the Society Help Desk project.
- What machine learning skills does she have?
- What is her CGPA?
- What certifications does she have?
- What is OAuth 2.0?
- Explain REST APIs.

---

## 📷 Application Workflow

```
User Question
       │
       ▼
 Streamlit Chat UI
       │
       ▼
Prompt + Resume Context
       │
       ▼
 Google Gemini API
       │
       ▼
 AI Response
```

---

## 📚 Learning Outcomes

This project helped me learn:

- Building AI-powered applications with Streamlit
- Prompt Engineering
- Using Google Gemini API
- Managing API keys securely with dotenv
- Creating conversational interfaces
- Integrating resume context with Large Language Models (LLMs)

---

## 🔮 Future Improvements

- Upload resume dynamically (PDF/DOCX)
- Conversation memory
- Voice interaction
- Deploy on Streamlit Cloud
- Support multiple resumes
- Better prompt engineering
- Resume download option

---

## 👩‍💻 Author

**Prachi Dhiman**

B.Tech Computer Science & Engineering

Interested in AI, Machine Learning, Full Stack Development, and Generative AI.

---

## ⭐ If you found this project useful, consider giving it a star!
