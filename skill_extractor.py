import re


# Skills used by the project
SKILLS = [
    "Python",
    "SQL",
    "Excel",
    "Pandas",
    "Power BI",
    "Machine Learning",
    "ML",
    "Scikit-learn",
    "FastAPI",
    "Docker",
    "Deep Learning",
    "LLM",
    "RAG",
    "APIs",
    "NLP",
    "Transformers",
    "Hugging Face",
    "OpenCV",
    "CNN",
    "YOLO",
    "NumPy"
]


def extract_skills(resume_text):
    """
    Extract skills found in the resume.
    """

    resume_text_lower = resume_text.lower()

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, resume_text_lower):
            found_skills.append(skill)

    return found_skills


def find_missing_skills(found_skills, required_skills):
    """
    Find skills required by a job but missing from the resume.
    """

    found_lower = {
        skill.lower()
        for skill in found_skills
    }

    missing_skills = []

    for skill in required_skills:

        if skill.lower() not in found_lower:
            missing_skills.append(skill)

    return missing_skills