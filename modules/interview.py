import streamlit as st
from google import genai
import os

QUESTIONS = {
    "Python": [
        "What are Python decorators?",
        "Difference between List and Tuple?",
        "What is *args and **kwargs?",
        "Explain OOP in Python.",
        "What are Python generators?"
    ],
    "SQL": [
        "What is JOIN?",
        "Difference between WHERE and HAVING?",
        "Explain Primary Key.",
        "What is Normalization?",
        "Difference between DELETE and TRUNCATE?"
    ],
    "Machine Learning": [
        "What is Overfitting?",
        "Difference between Supervised and Unsupervised Learning?",
        "Explain Random Forest.",
        "What is Cross Validation?",
        "Difference between Classification and Regression?"
    ],
    "HR Interview": [
        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your strengths?",
        "What are your weaknesses?",
        "Where do you see yourself in 5 years?"
    ]
}
def generate_ai_interview(role, experience, interview_type):

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = f"""
    You are an expert technical interviewer.

    Generate a professional interview for:

    Job Role: {role}
    : {experience}
    Interview Type: {interview_type}

    Provide:

    # Interview Questions

    For each of the 5 questions include:

    Question:
    Ideal Answer:
    Interview Tip:

    Finally provide:

    # Overall Interview Advice

    Return everything in Markdown.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


def interview_page():

    st.subheader("🎤 Interview Preparation")

    category = st.selectbox(
        "Select Interview Category",
        list(QUESTIONS.keys())
    )

    st.divider()

    st.subheader("📋 Practice Questions")

    for i, question in enumerate(QUESTIONS[category], start=1):
        st.info(f"{i}. {question}")
    st.divider()

st.subheader("🤖 AI Interview Coach")

job_role = st.text_input(
    "Job Role",
    placeholder="e.g. AI Engineer"
)

experience = st.selectbox(
    "Experience Level",
    [
        "Fresher",
        "1-3 Years",
        "3-5 Years",
        "5+ Years"
    ]
)

interview_type = st.selectbox(
    "Interview Type",
    [
        "Technical",
        "HR",
        "Behavioral",
        "Mixed"
    ]
)

if st.button("🚀 Generate AI Interview"):

    if job_role.strip() == "":
        st.warning("Please enter a job role.")
    else:

        with st.spinner("Generating Interview..."):

            result = generate_ai_interview(
                job_role,
                experience,
                interview_type
            )

        st.success("Interview Generated Successfully!")

        st.markdown(result)