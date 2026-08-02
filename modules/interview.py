import streamlit as st


def interview_page():
    st.subheader("🎤 AI Interview Preparation")

    st.write(
        "Prepare for your interviews by generating common interview questions."
    )

    job_role = st.selectbox(
        "Select Job Role",
        [
            "Software Engineer",
            "Data Scientist",
            "Machine Learning Engineer",
            "Web Developer",
            "Python Developer",
            "AI Engineer"
        ]
    )

    if st.button("Generate Interview Questions"):

        st.success(f"Interview Questions for {job_role}")

        questions = [
            "Tell me about yourself.",
            "Why do you want this role?",
            "What are your strengths?",
            "What are your weaknesses?",
            "Describe one challenging project you completed.",
            "What programming languages do you know?",
            "Explain one project from your resume.",
            "Why should we hire you?",
            "Where do you see yourself in five years?",
            "Do you have any questions for us?"
        ]

        for i, question in enumerate(questions, start=1):
            st.markdown(f"**{i}. {question}**")

        st.info(
            "💡 Tip: Practice answering these questions aloud before your interview."
        )