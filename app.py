# ==========================================
# AI Career Assistant
# Main Application File
# Developed by: Aqsa Awan
# ==========================================

import os
import streamlit as st
import pdfplumber

from utils.ats_checker import (
    calculate_ats_score,
    get_score_breakdown
)

from modules.cover_letter import cover_letter_page
from modules.interview import interview_page
from modules.resume_match import resume_match_page

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

/* Background */
.stApp{
    background:linear-gradient(135deg,#eef4ff,#f8fbff);
}

/* Main Container */
.block-container{
    max-width:1200px;
    padding-top:2rem;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0f172a;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Buttons */
.stButton>button{
    background:linear-gradient(90deg,#2563eb,#3b82f6);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px 20px;
    font-weight:700;
}

.stButton>button:hover{
    transform:translateY(-2px);
}

/* Metric Cards */
[data-testid="metric-container"]{
    border-radius:15px;
    background:white;
    padding:15px;
    box-shadow:0 5px 18px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# PDF Reader
# ==========================================

def extract_pdf_text(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# ==========================================
# Temporary AI Analyzer
# ==========================================

def analyze_resume_with_ai(resume_text):

    return """
# 📊 Resume Analysis

### ✅ Resume Score
78 / 100

### 💪 Strengths
- Good Resume Structure
- Projects Included
- Education Section Present

### ⚠️ Improvements
- Add more technical skills
- Improve ATS keywords
- Mention achievements
- Add LinkedIn & GitHub

### 🚀 ATS Tips
- Tailor resume for every job
- Use action verbs
- Keep formatting simple
"""


# ==========================================
# Landing Page
# ==========================================

st.title("🤖 AI Career Assistant")

feature1, feature2 = st.columns(2)

with feature1:
    st.success("📄 Resume Analyzer")
    st.success("🎯 ATS Checker")
    st.success("💼 Cover Letter Generator")

with feature2:
    st.success("🎤 Interview Preparation")
    st.success("📊 Resume Match")
    st.success("🤖 Career Guidance")

# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.header("📋 Navigation")

    selected_page = st.radio(
        "Choose a Feature",
        [
            "🏠 Home",
            "📄 Resume Analyzer",
            "🎯 ATS Checker",
            "💼 Cover Letter Generator",
            "🎤 Interview Preparation",
            "📊 Resume vs Job Description"
        ]
    )

# ==========================================
# Home
# ==========================================

if selected_page == "🏠 Home":

    left, right = st.columns([1.2, 1])

    with left:

        st.title("🤖 AI Career Assistant")

        st.markdown("""
### Build Smarter Resumes. Land Better Jobs.

Your all-in-one AI-powered platform to:

✅ Analyze resumes

✅ Improve ATS Score

✅ Generate Cover Letters

✅ Practice Interviews

✅ Match Resume with Job Descriptions

---

Start exploring using the sidebar.
""")

        st.success("🚀 Powered by Artificial Intelligence")

    with right:

        st.image(
            "assets/home.png",
            use_container_width=True
        )

    st.markdown("---")

    st.subheader("✨ Explore Features")

    space1, main, space2 = st.columns([1, 6, 1])

    with main:

        col1, col2, col3 = st.columns(3)

        with col1:
            st.info(
                "📄 Resume Analyzer\n\nAnalyze your resume and receive AI-powered suggestions."
            )

        with col2:
            st.info(
                "🎯 ATS Checker\n\nCheck how ATS-friendly your resume is."
            )

        with col3:
            st.info(
                "💼 Cover Letter\n\nGenerate professional cover letters instantly."
            )

        col4, col5, col6 = st.columns(3)

        with col4:
            st.info(
                "🎤 Interview Prep\n\nPractice common interview questions."
            )

        with col5:
            st.info(
                "📊 Resume Match\n\nCompare your resume with any job description."
            )

        with col6:
            st.info(
                "🤖 AI Career Guide\n\nReceive personalized career recommendations."
            )


# ==========================================
# ATS Checker
# ==========================================

elif selected_page == "🎯 ATS Checker":

    st.image(
        "assets/ats.png",
        use_container_width=True
    )

    st.subheader("🎯 ATS Checker")

    st.info("🚧 This feature is coming soon.")


# ==========================================
# Cover Letter Generator
# ==========================================

elif selected_page == "💼 Cover Letter Generator":

    st.image(
        "assets/cover_letter.png",
        use_container_width=True
    )

    cover_letter_page()


# ==========================================
# Interview Preparation
# ==========================================

elif selected_page == "🎤 Interview Preparation":

    st.image(
        "assets/interview.png",
        use_container_width=True
    )

    interview_page()


# ==========================================
# Resume vs Job Description
# ==========================================

elif selected_page == "📊 Resume vs Job Description":

    st.image(
        "assets/resume_match.png",
        use_container_width=True
    )

    resume_match_page()


# ==========================================
# Footer
# ==========================================

st.divider()

st.markdown(
    """
<div style="text-align:center;color:gray;font-size:15px;">
© 2026 <b>AI Career Assistant</b> |
Developed with ❤️ by <b>Aqsa Awan</b>
</div>
""",
    unsafe_allow_html=True
)