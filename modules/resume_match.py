import streamlit as st


def resume_match_page():
    st.subheader("📊 Resume vs Job Description")

    st.write(
        "Compare your resume with a job description to estimate your match."
    )

    resume_text = st.text_area(
        "📄 Paste Resume Text",
        height=200
    )

    job_description = st.text_area(
        "💼 Paste Job Description",
        height=200
    )

    if st.button("Compare Resume"):

        if not resume_text or not job_description:
            st.warning("Please enter both Resume and Job Description.")
            return

        resume_words = set(resume_text.lower().split())
        jd_words = set(job_description.lower().split())

        common_words = resume_words.intersection(jd_words)

        if len(jd_words) == 0:
            match_score = 0
        else:
            match_score = int((len(common_words) / len(jd_words)) * 100)

        match_score = min(match_score, 100)

        st.metric("📈 Match Score", f"{match_score}%")

        st.progress(match_score / 100)

        if match_score >= 80:
            st.success("Excellent match! Your resume closely matches the job description.")

        elif match_score >= 60:
            st.warning("Good match, but you can improve your resume.")

        else:
            st.error("Low match. Consider updating your resume with relevant skills.")

        st.subheader("🛠 Common Keywords")

        if common_words:
            for word in sorted(common_words):
                st.success(word)
        else:
            st.warning("No common keywords found.")