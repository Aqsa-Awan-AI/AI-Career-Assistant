# ==========================================
# AI Career Assistant
# Main Application File
# Developed by: Aqsa Awan
# ==========================================

import os
import streamlit as st
import pdfplumber
from google import genai

# ==========================================
# Page Configuration
# (MUST be the very first Streamlit command)
# ==========================================

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

from utils.ats_checker import (
    calculate_ats_score,
    get_score_breakdown
)

from modules.cover_letter import cover_letter_page
from modules.interview import interview_page
from modules.resume_match import resume_match_page
from modules.career_guidance import career_guidance_page

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

    prompt = f"""
You are an expert ATS Resume Reviewer and Career Coach.

Analyze the following resume professionally.

Return your response in Markdown.

Include these sections:

# ATS Score (0-100)

# Strengths

# Weaknesses

# Missing Skills

# Suggestions for Improvement

# Recommended Job Roles

# Final Verdict

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


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
            "📊 Resume vs Job Description",
            "🤖 Career Guidance"
        ]
    )

# ==========================================
# Home
# ==========================================

if selected_page == "🏠 Home":

    left, right = st.columns([1, 1.6])

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

        try:
            resume_text = extract_pdf_text(uploaded_resume)
        except Exception as e:
            st.error("⚠️ Could not read this PDF. Please make sure it's not corrupted or password-protected.")
            st.stop()

        if not resume_text.strip():
            st.warning("⚠️ No readable text found in this PDF. It may be a scanned image — try a text-based PDF instead.")
            st.stop()

        st.success("✅ Resume uploaded successfully!")

        st.subheader("📄 Extracted Resume")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

        st.markdown("---")

        st.subheader("🤖 AI Resume Analysis")

        if st.button("Analyze Resume"):

            with st.spinner("Analyzing your resume using Gemini AI..."):

                try:
                    result = analyze_resume_with_ai(resume_text)
                    st.success("✅ Analysis Completed!")
                    st.markdown(result)

                except Exception as e:
                    st.error(
                        "⚠️ Something went wrong while analyzing your resume. "
                        "Please try again in a moment."
                    )
                    st.caption(f"Technical details: {e}")


# ==========================================
# ATS Checker
# ==========================================

elif selected_page == "🎯 ATS Checker":

    st.image(
        "assets/ats.png",
        use_container_width=True
    )

    st.subheader("🎯 ATS Checker")

    st.write(
        "Upload your resume and check how strong it is according to the "
        "ATS (Applicant Tracking System)."
    )

    uploaded_resume_ats = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"],
        key="ats_uploader"
    )

    if uploaded_resume_ats is not None:

        try:
            resume_text_ats = extract_pdf_text(uploaded_resume_ats)
        except Exception as e:
            st.error("⚠️ Could not read this PDF. Please make sure it's not corrupted or password-protected.")
            st.stop()

        if not resume_text_ats.strip():
            st.warning("⚠️ No readable text found in this PDF. It may be a scanned image — try a text-based PDF instead.")
            st.stop()

        st.success("✅ Resume uploaded successfully!")

        if st.button("🎯 Check ATS Score"):

            with st.spinner("Calculating ATS Score..."):

                score, found_skills = calculate_ats_score(resume_text_ats)
                breakdown = get_score_breakdown(resume_text_ats)

            st.markdown("---")

            # Overall Score
            col1, col2 = st.columns([1, 2])

            with col1:
                st.metric("📊 Overall ATS Score", f"{score}/100")

            with col2:
                st.progress(score / 100)

                if score >= 80:
                    st.success("Excellent! Your resume is highly ATS-friendly.")
                elif score >= 50:
                    st.warning("Decent score, but there's room for improvement.")
                else:
                    st.error("Low ATS score. Consider adding more relevant keywords.")

            st.markdown("---")

            # Score Breakdown
            st.subheader("📋 Score Breakdown")

            b1, b2, b3, b4 = st.columns(4)

            with b1:
                st.metric("🛠 Technical Skills", f"{breakdown['Technical Skills']}/50")

            with b2:
                st.metric("🎓 Education", f"{breakdown['Education']}/15")

            with b3:
                st.metric("💼 Projects", f"{breakdown['Projects']}/20")

            with b4:
                st.metric("📈 Experience", f"{breakdown['Experience']}/15")

            st.markdown("---")

            # Found Skills
            st.subheader("✅ Skills Detected in Your Resume")

            if found_skills:
                skill_cols = st.columns(len(found_skills)) if len(found_skills) <= 5 else st.columns(5)
                for i, skill in enumerate(found_skills):
                    with skill_cols[i % len(skill_cols)]:
                        st.info(f"✔ {skill.title()}")
            else:
                st.warning(
                    "No common technical skills detected. Try adding relevant "
                    "keywords like Python, SQL, Machine Learning, etc."
                )

    else:
        st.info("👆 Please upload your resume to get started.")


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
# Career Guidance
# ==========================================

elif selected_page == "🤖 Career Guidance":

    career_guidance_page()

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