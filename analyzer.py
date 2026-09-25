# ==========================================
# AI RESUME ANALYZER
# analyzer.py
# ==========================================


# ==========================================
# 1. SKILL ANALYSIS
# ==========================================

def analyze_resume(resume_text):

    skills_list = [
        "Python",
        "C",
        "C++",
        "Java",
        "Artificial Intelligence",
        "AI",
        "Machine Learning",
        "Deep Learning",
        "VLSI",
        "IoT",
        "Embedded Systems",
        "MATLAB",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Verilog",
        "Django",
        "Flask",
        "Git",
        "Excel",
        "Data Analysis",
        "Digital Electronics",
        "Communication Systems",
        "Computer Networks"
    ]

    found_skills = []

    for skill in skills_list:

        if skill.lower() in resume_text.lower():

            found_skills.append(skill)

    return found_skills


# ==========================================
# 2. RESUME SCORE
# ==========================================

def calculate_resume_score(resume_text, skills):

    score = 0

    # --------------------------------------
    # Skills
    # --------------------------------------

    if len(skills) >= 5:
        score += 30

    elif len(skills) >= 3:
        score += 20

    elif len(skills) >= 1:
        score += 10


    # --------------------------------------
    # Education
    # --------------------------------------

    resume_lower = resume_text.lower()

    if "education" in resume_lower:
        score += 15


    # --------------------------------------
    # Projects
    # --------------------------------------

    if "project" in resume_lower:
        score += 15


    # --------------------------------------
    # Experience
    # --------------------------------------

    if "experience" in resume_lower:
        score += 10


    # --------------------------------------
    # Certification
    # --------------------------------------

    if "certification" in resume_lower:
        score += 10


    # --------------------------------------
    # Achievement
    # --------------------------------------

    if "achievement" in resume_lower or "award" in resume_lower:
        score += 10


    # Maximum score = 100

    if score > 100:
        score = 100

    return score


# ==========================================
# 3. MISSING SKILLS
# ==========================================

def get_missing_skills(resume_text):

    important_skills = [
        "Python",
        "C",
        "C++",
        "Java",
        "Machine Learning",
        "Deep Learning",
        "SQL",
        "HTML",
        "CSS",
        "JavaScript",
        "Git",
        "Django",
        "Flask",
        "Verilog",
        "MATLAB"
    ]

    missing_skills = []

    resume_lower = resume_text.lower()

    for skill in important_skills:

        if skill.lower() not in resume_lower:
            missing_skills.append(skill)

    return missing_skills


# ==========================================
# 4. RESUME IMPROVEMENT SUGGESTIONS
# ==========================================

def generate_suggestions(resume_text, skills):

    suggestions = []

    resume_lower = resume_text.lower()


    # --------------------------------------
    # Education
    # --------------------------------------

    if "education" not in resume_lower:

        suggestions.append(
            "Add an Education section."
        )


    # --------------------------------------
    # Skills
    # --------------------------------------

    if len(skills) < 5:

        suggestions.append(
            "Add more relevant technical skills."
        )


    # --------------------------------------
    # Projects
    # --------------------------------------

    if "project" not in resume_lower:

        suggestions.append(
            "Add your academic or personal projects."
        )


    # --------------------------------------
    # Experience
    # --------------------------------------

    if "experience" not in resume_lower:

        suggestions.append(
            "Add internship or work experience if available."
        )


    # --------------------------------------
    # Certification
    # --------------------------------------

    if "certification" not in resume_lower:

        suggestions.append(
            "Add relevant certifications."
        )


    # --------------------------------------
    # Achievement
    # --------------------------------------

    if (
        "achievement" not in resume_lower
        and "award" not in resume_lower
    ):

        suggestions.append(
            "Add your achievements or awards."
        )


    # --------------------------------------
    # Technical Skills
    # --------------------------------------

    if len(skills) < 8:

        suggestions.append(
            "Add more relevant technical skills."
        )


    # --------------------------------------
    # If no suggestions
    # --------------------------------------

    if len(suggestions) == 0:

        suggestions.append(
            "Your resume has a good basic structure. "
            "Keep improving it with measurable achievements."
        )


    return suggestions


# ==========================================
# 5. JOB ROLE MATCHING
# ==========================================

def job_role_match(resume_text):

    # --------------------------------------
    # Job roles and required skills
    # --------------------------------------

    job_roles = {

        "Python Developer": [
            "Python",
            "SQL",
            "Django",
            "Flask",
            "Git"
        ],

        "AI/ML Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "Artificial Intelligence",
            "AI"
        ],

        "Embedded Engineer": [
            "C",
            "C++",
            "Embedded Systems",
            "IoT",
            "Digital Electronics"
        ],

        "VLSI Engineer": [
            "VLSI",
            "Verilog",
            "Digital Electronics",
            "MATLAB",
            "C"
        ],

        # ----------------------------------
        # 5th JOB ROLE
        # ----------------------------------

        "Data Analyst": [
            "Python",
            "SQL",
            "MATLAB",
            "Excel",
            "Data Analysis"
        ]
    }


    # --------------------------------------
    # Convert resume to lowercase
    # --------------------------------------

    resume_lower = resume_text.lower()


    role_results = {}


    # --------------------------------------
    # Calculate percentage for each role
    # --------------------------------------

    for role, required_skills in job_roles.items():

        matched_skills = 0

        for skill in required_skills:

            if skill.lower() in resume_lower:

                matched_skills += 1


        # Calculate percentage

        percentage = (
            matched_skills / len(required_skills)
        ) * 100


        role_results[role] = int(percentage)


    return role_results


# ==========================================
# END OF analyzer.py
# ==========================================