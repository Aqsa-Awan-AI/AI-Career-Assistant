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

    st.image(
        "assets/home.png",
        use_container_width=True
    )

    st.subheader("🏠 AI Career Assistant")

    st.markdown("""
### Build Smarter Resumes. Land Better Jobs. 🚀

Welcome to your AI-powered career assistant.

Use the sidebar to explore all AI tools.
""")

# ==========================================
# Resume Analyzer
# ==========================================

elif selected_page == "📄 Resume Analyzer":

    st.image(
        "assets/resume.png",
        use_container_width=True
    )

    st.subheader("📄 Resume Analyzer")

    uploaded_resume = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_resume is not None:

        st.success("✅ Resume uploaded successfully!")

        st.write("**File Name:**", uploaded_resume.name)

        st.write(
            "**File Size:**",
            round(uploaded_resume.size / 1024, 2),
            "KB"
        )

        resume_text = extract_pdf_text(uploaded_resume)

        ats_score, found_skills = calculate_ats_score(
            resume_text
        )

        breakdown = get_score_breakdown(
            resume_text
        )

        st.subheader("📄 Extracted Resume")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

        st.subheader("📊 Resume Statistics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Words",
                len(resume_text.split())
            )

        with col2:
            st.metric(
                "Characters",
                len(resume_text)
            )

        with col3:
            st.metric(
                "Skills",
                len(found_skills)
            )

        st.subheader("📋 Score Breakdown")

        left, right = st.columns(2)

        with left:
            st.info(
                f"🛠 Technical Skills : {breakdown['Technical Skills']}/50"
            )
            st.info(
                f"🎓 Education : {breakdown['Education']}/15"
            )

        with right:
            st.info(
                f"📁 Projects : {breakdown['Projects']}/20"
            )
            st.info(
                f"💼 Experience : {breakdown['Experience']}/15"
            )

        st.subheader("🎯 ATS Score")

        st.metric(
            "Overall Score",
            f"{ats_score}/100"
        )

        st.progress(ats_score / 100)

        st.subheader("🛠 Skills Found")

        if found_skills:

            for skill in found_skills:
                st.success(skill.title())

        else:

            st.warning("No matching skills found.")

        st.subheader("🤖 AI Analysis")

        if st.button("Analyze Resume"):

            st.info("Analyzing Resume...")

            result = analyze_resume_with_ai(
                resume_text
            )

            st.success("Analysis Completed!")

            st.markdown(result)


# ==========================================
# ATS Checker
# ==========================================

elif selected_page == "🎯 ATS Checker":

    st.image(
        "assets/ats.png",
        use_container_width=True
    )

    st.subheader("🎯 ATS Checker")

    st.info(
        "🚧 This feature is coming soon."
    )


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