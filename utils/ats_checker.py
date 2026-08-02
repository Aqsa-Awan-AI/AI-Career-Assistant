# ==========================================
# ATS Checker Module
# Developed by: Aqsa Awan
# ==========================================

def calculate_ats_score(resume_text):
    """
    Calculate a simple ATS score based on resume content.
    """

    score = 0

    resume_text = resume_text.lower()

    # -----------------------------
    # Technical Skills
    # -----------------------------
    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "pandas",
        "numpy",
        "streamlit",
        "github"
    ]

    found_skills = []

    for skill in skills:

        if skill in resume_text:
            score += 5
            found_skills.append(skill)

    # Maximum 50 marks for skills
    if score > 50:
        score = 50

    # -----------------------------
    # Education
    # -----------------------------
    if "bs" in resume_text or "bachelor" in resume_text:
        score += 15

    # -----------------------------
    # Projects
    # -----------------------------
    if "project" in resume_text:
        score += 20

    # -----------------------------
    # Experience
    # -----------------------------
    if "internship" in resume_text or "experience" in resume_text:
        score += 15

    # -----------------------------
    # Limit Score
    # -----------------------------
    if score > 100:
        score = 100

    return score, found_skills


# ------------------------------------------
# Detailed ATS Score Breakdown
# ------------------------------------------
def get_score_breakdown(resume_text):

    resume_text = resume_text.lower()

    breakdown = {
        "Technical Skills": 0,
        "Education": 0,
        "Projects": 0,
        "Experience": 0
    }

    # Technical Skills
    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "streamlit",
        "github",
        "pandas",
        "numpy"
    ]

    for skill in skills:
        if skill in resume_text:
            breakdown["Technical Skills"] += 5

    breakdown["Technical Skills"] = min(
        breakdown["Technical Skills"], 50
    )

    # Education
    if "bs" in resume_text or "bachelor" in resume_text:
        breakdown["Education"] = 15

    # Projects
    if "project" in resume_text:
        breakdown["Projects"] = 20

    # Experience
    if "internship" in resume_text or "experience" in resume_text:
        breakdown["Experience"] = 15

    return breakdown