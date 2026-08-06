import os
import streamlit as st
from google import genai


def generate_career_guidance(skills, interests, education, experience_level):

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = f"""
You are an expert career counselor and industry advisor.

Based on the following profile, suggest suitable career paths.

Skills: {skills}
Interests: {interests}
Education: {education}
Experience Level: {experience_level}

Return your response in clean Markdown format with these sections:

# Recommended Career Paths
(List 3-5 suitable job roles with a short reason for each)

# Skills You Should Improve
(List specific skills to learn or strengthen)

# Suggested Learning Resources
(Types of courses, certifications, or platforms to explore)

# Industry Outlook
(Brief note on demand and growth for these career paths)

# Final Advice
(A short motivating summary)
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


def career_guidance_page():

    st.subheader("🤖 AI Career Guidance")

    st.write(
        "Tell us about yourself and get personalized career path "
        "recommendations powered by AI."
    )

    skills = st.text_area(
        "🛠 Your Skills",
        placeholder="e.g. Python, SQL, Communication, Data Analysis..."
    )

    interests = st.text_area(
        "❤️ Your Interests",
        placeholder="e.g. Artificial Intelligence, Design, Finance..."
    )

    education = st.text_input(
        "🎓 Education",
        placeholder="e.g. BS Computer Science"
    )

    experience_level = st.selectbox(
        "📈 Experience Level",
        [
            "Student / Fresher",
            "1-3 Years",
            "3-5 Years",
            "5+ Years"
        ]
    )

    if st.button("🚀 Get Career Guidance"):

        if not skills or not interests or not education:
            st.warning("Please fill in your skills, interests, and education.")

        else:

            with st.spinner("Analyzing your profile and generating guidance..."):

                try:

                    result = generate_career_guidance(
                        skills,
                        interests,
                        education,
                        experience_level
                    )

                    st.success("✅ Career Guidance Generated Successfully!")

                    st.markdown(result)

                    st.download_button(
                        label="📥 Download Career Guidance Report",
                        data=result,
                        file_name="Career_Guidance_Report.txt",
                        mime="text/plain"
                    )

                except Exception as e:

                    st.error(f"Error: {e}")