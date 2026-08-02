import streamlit as st


def cover_letter_page():

    st.subheader("💼 AI Cover Letter Generator")

    st.write(
        "Fill in the details below to generate a professional cover letter."
    )

    full_name = st.text_input("👤 Full Name")

    job_role = st.text_input("💼 Job Role")

    company = st.text_input("🏢 Company Name")

    skills = st.text_area(
        "🛠 Skills",
        placeholder="Python, SQL, Machine Learning, Communication..."
    )

    experience = st.text_area(
        "📄 Experience / Projects",
        placeholder="Describe your experience..."
    )

    if st.button("Generate Cover Letter"):

        if not full_name or not job_role or not company:

            st.warning("Please fill all required fields.")

        else:

            letter = f"""
Dear Hiring Manager,

I am writing to express my interest in the {job_role} position at {company}.

My name is {full_name}, and I have developed skills in {skills}.

My experience includes:

{experience}

I am passionate about learning new technologies and contributing to meaningful projects. I believe my skills and dedication make me a strong candidate for this position.

Thank you for considering my application. I look forward to the opportunity to discuss my qualifications further.

Sincerely,

{full_name}
"""

            st.success("✅ Cover Letter Generated Successfully!")

            st.text_area(
                "Generated Cover Letter",
                letter,
                height=350
            )