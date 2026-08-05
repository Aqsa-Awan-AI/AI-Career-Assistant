# 🤖 AI Career Assistant

An AI-powered web application that helps students and professionals improve their resumes, evaluate ATS compatibility, and receive career guidance.

---

## 📌 Project Overview

AI Career Assistant is a Streamlit-based application designed to simplify resume analysis and career preparation. It extracts resume content from PDF files, calculates an ATS score, generates cover letters, preps users for interviews, matches resumes against job descriptions, and provides AI-powered career guidance — all powered by Google's Gemini AI.

---

## ✨ Features

- 📄 AI Resume Analyzer (Gemini-powered feedback)
- 🎯 ATS Score Checker with detailed breakdown
- 💼 AI Cover Letter Generator
- 🎤 AI-Powered Interview Preparation
- 📊 Resume vs Job Description Matching
- 🤖 AI Career Guidance (personalized career path recommendations)
- 🖼️ Professional UI with Feature Illustrations

---

## 📸 Screenshots

### 🏠 Home

![Home](screenshots/home.png)

### 📄 Resume Analyzer

![Resume](screenshots/resume.png)

### 🎯 ATS Checker

![ATS](screenshots/ats.png)

### 💼 Cover Letter Generator

![Cover Letter](screenshots/cover_letter.png)

### 🎤 Interview Preparation

![Interview](screenshots/interview.png)

### 📊 Resume vs Job Description

![Resume Match](screenshots/resume_match.png)

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini AI (google-genai)
- PDFPlumber
- Git & GitHub

---

## 📂 Project Structure

AI-Career-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│ ├── config.toml
│ └── secrets.toml
├── assets/
├── modules/
│ ├── cover_letter.py
│ ├── interview.py
│ ├── resume_match.py
│ └── career_guidance.py
└── utils/
└── ats_checker.py

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Aqsa-Awan-AI/AI-Career-Assistant.git
```

Move into the project directory:

```bash
cd AI-Career-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your Gemini API key in `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Current Progress

- ✅ Resume PDF Upload & Text Extraction
- ✅ AI Resume Analysis (Gemini)
- ✅ ATS Score Calculation with Breakdown
- ✅ Skills Detection
- ✅ AI Cover Letter Generator
- ✅ AI Interview Question Generator
- ✅ Resume vs Job Description Matching
- ✅ AI Career Guidance

---

## 🔮 Future Improvements

- Resume Download Feature (PDF export)
- Multi-language Resume Support
- User Authentication & Saved History
- Resume Builder Templates

---

## 👩‍💻 Author

**Aqsa Awan**

AI & Machine Learning Enthusiast

GitHub:
https://github.com/Aqsa-Awan-AI

LinkedIn:
https://www.linkedin.com/in/aqsa-awan-ai/

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.