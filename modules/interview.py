import streamlit as st

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