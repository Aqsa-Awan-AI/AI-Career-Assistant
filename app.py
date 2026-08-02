# ==========================================
# AI Career Assistant
# Main Application File
# Developed by: Aqsa Awan
# ==========================================

# ------------------------------------------
# Import Required Libraries
# ------------------------------------------
import streamlit as st
import pdfplumber

from utils.ats_checker import (
    calculate_ats_score,
    get_score_breakdown
)
from modules.cover_letter import cover_letter_page
from modules.interview import interview_page
from modules.resume_match import resume_match_page

# ------------------------------------------
# Configure Streamlit Page
# ------------------------------------------
st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)


# ------------------------------------------
# PDF Text Extraction Function
# ------------------------------------------
def extract_pdf_text(uploaded_file):
    """
    Extract text from uploaded PDF.
    """

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# ------------------------------------------
# Temporary AI Resume Analyzer
# ------------------------------------------
def analyze_resume_with_ai(resume_text):
    """
    Temporary AI analysis.
    Gemini API will be connected later.
    """

    return """
# 📊 Resume Analysis

### ✅ Resume Score
**78 / 100**

## 💪 Strengths

- Good overall resume structure.
- Projects section is included.
- Education details are clear.
- Resume is readable.

## ⚠️ Areas for Improvement

- Add more technical skills.
- Mention measurable achievements.
- Improve ATS keywords.
- Add GitHub profile.
- Add LinkedIn profile.

## 🚀 ATS Suggestions

- Use action verbs.
- Keep formatting simple.
- Tailor resume for each job.
- Include relevant keywords from job descriptions.

---

This is a demo AI analysis.
Gemini AI integration will be enabled later.
"""


# ==========================================
# Main Page
# ==========================================

st.title("🤖 AI Career Assistant")

st.markdown(
    """
Welcome to the next-generation **AI Career Assistant**.

This application helps students and professionals improve their careers using Artificial Intelligence.
"""
)

# ------------------------------------------
# Features
# ------------------------------------------

feature_col1, feature_col2 = st.columns(2)

with feature_col1:

    st.success("📄 Resume Analysis")
    st.success("🎯 ATS Score Checker")
    st.success("💼 Cover Letter Generator")

with feature_col2:

    st.success("🎤 Interview Preparation")
    st.success("📊 Resume vs Job Description")
    st.success("🤖 AI Career Guidance")


# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.header("📋 Navigation")

    selected_page = st.radio(
        "Choose a feature:",
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

    st.subheader("🏠 Home")

    st.info(
        "Welcome to the AI Career Assistant!"
    )


# ==========================================
# Resume Analyzer
# ==========================================

elif selected_page == "📄 Resume Analyzer":

    st.subheader("📄 Resume Analyzer")

    uploaded_resume = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_resume is not None:

        st.success("✅ Resume uploaded successfully!")

        st.write(
            "**File Name:**",
            uploaded_resume.name
        )

        st.write(
            "**File Size:**",
            round(uploaded_resume.size / 1024, 2),
            "KB"
        )

        # ------------------------------------------
        # Extract Resume Text
        # ------------------------------------------

        resume_text = extract_pdf_text(uploaded_resume)

        # ------------------------------------------
        # ATS Score
        # ------------------------------------------

        ats_score, found_skills = calculate_ats_score(
            resume_text
        )

        breakdown = get_score_breakdown(
            resume_text
        )

        # ------------------------------------------
        # Resume Text
        # ------------------------------------------

        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

        # ------------------------------------------
        # Resume Statistics
        # ------------------------------------------

        st.subheader("📊 Resume Statistics")

        stat_col1, stat_col2, stat_col3 = st.columns(3)

        with stat_col1:
            st.metric(
                "Total Words",
                len(resume_text.split())
            )

        with stat_col2:
            st.metric(
                "Characters",
                len(resume_text)
            )

        with stat_col3:
            st.metric(
                "Skills Found",
                len(found_skills)
            )

        # ------------------------------------------
        # Score Breakdown
        # ------------------------------------------

        st.subheader("📋 Score Breakdown")

        breakdown_col1, breakdown_col2 = st.columns(2)

        with breakdown_col1:

            st.info(
                f"🛠 Technical Skills: {breakdown['Technical Skills']}/50"
            )

            st.info(
                f"🎓 Education: {breakdown['Education']}/15"
            )

        with breakdown_col2:

            st.info(
                f"📁 Projects: {breakdown['Projects']}/20"
            )

            st.info(
                f"💼 Experience: {breakdown['Experience']}/15"
            )

        # ------------------------------------------
        # ATS Score
        # ------------------------------------------

        st.subheader("🎯 ATS Score")

        st.metric(
            label="Overall ATS Score",
            value=f"{ats_score}/100"
        )

        st.progress(ats_score / 100)

        # ------------------------------------------
        # ATS Dashboard
        # ------------------------------------------
        st.subheader("📈 ATS Dashboard")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("ATS Score", f"{ats_score}/100")

        with col2:
            st.metric("Skills Found", len(found_skills))

        with col3:
            st.metric("Resume Words", len(resume_text.split()))

        if ats_score >= 80:

            st.success(
                "🎉 Excellent! Your resume is highly ATS-friendly."
            )

        elif ats_score >= 60:

            st.warning(
                "👍 Good resume, but there is room for improvement."
            )

        else:

            st.error(
                "⚠️ Your resume needs significant ATS improvements."
            )

        # ------------------------------------------
        # Skills Found
        # ------------------------------------------

        st.subheader("🛠 Skills Found")

        if found_skills:

            for skill in found_skills:

                st.success(skill.title())

        else:

            st.warning(
                "No matching skills found."
            )

# ------------------------------------------
# AI Analysis
# ------------------------------------------

        st.subheader("🤖 AI Analysis")

        if st.button("Analyze Resume"):

            st.info("Analyzing resume...")

            result = analyze_resume_with_ai(
                resume_text
            )

            st.success("Analysis Completed!")

            st.markdown(result)


# ==========================================
# ATS Checker
# ==========================================

elif selected_page == "🎯 ATS Checker":

    st.subheader("🎯 ATS Checker")

    st.info("Coming Soon...")


# ==========================================
# Interview Preparation
# ==========================================

elif selected_page == "🎤 Interview Preparation":

    interview_page()


# ==========================================
# Resume vs Job Description
# ==========================================

elif selected_page == "📊 Resume vs Job Description":

    resume_match_page()


# ==========================================
# Cover Letter Generator
# ==========================================

elif selected_page == "💼 Cover Letter Generator":

    cover_letter_page()


# ==========================================
# Footer
# ==========================================

st.divider()

st.caption(
    "© 2026 AI Career Assistant | Developed by Aqsa Awan"
)