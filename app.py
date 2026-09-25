import streamlit as st
import pandas as pd
from pypdf import PdfReader
from docx import Document

from skill_extractor import extract_skills, find_missing_skills
from job_matcher import recommend_jobs
from roadmap_generator import generate_roadmap


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ==================================================
# TITLE
# ==================================================

st.title("📄 AI Resume Analyzer & Job Recommendation System")

st.write(
    "Upload your resume and find suitable job roles, "
    "matching scores, missing skills, and a learning roadmap."
)


# ==================================================
# RESUME TEXT EXTRACTION
# ==================================================

def extract_pdf_text(uploaded_file):

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_docx_text(uploaded_file):

    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text


# ==================================================
# FILE UPLOAD
# ==================================================

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


# ==================================================
# MAIN APPLICATION
# ==================================================

if uploaded_file is not None:

    st.success(
        f"Resume uploaded successfully: {uploaded_file.name}"
    )


    # ==================================================
    # EXTRACT RESUME TEXT
    # ==================================================

    if uploaded_file.name.lower().endswith(".pdf"):

        resume_text = extract_pdf_text(uploaded_file)

    else:

        resume_text = extract_docx_text(uploaded_file)


    # ==================================================
    # CHECK RESUME TEXT
    # ==================================================

    if not resume_text.strip():

        st.error(
            "Could not extract text from this resume."
        )

    else:

        # ==================================================
        # EXTRACT SKILLS
        # ==================================================

        found_skills = extract_skills(
            resume_text
        )


        # ==================================================
        # DISPLAY SKILLS
        # ==================================================

        st.header("🛠️ Skills Found in Resume")

        if found_skills:

            for skill in found_skills:

                st.write(
                    f"✓ {skill}"
                )

        else:

            st.warning(
                "No skills were detected."
            )


        # ==================================================
        # JOB RECOMMENDATIONS
        # ==================================================

        st.header("💼 Job Recommendations")

        results = recommend_jobs(
            resume_text
        )


        # Convert results to DataFrame

        results_df = pd.DataFrame(
            results
        )


        # ==================================================
        # DISPLAY ALL MATCH SCORES
        # ==================================================

        st.subheader("📊 Match Scores")

        st.dataframe(
            results_df,
            use_container_width=True
        )


        # ==================================================
        # TOP 3 RECOMMENDED JOBS
        # ==================================================

        st.subheader(
            "🏆 Top 3 Recommended Jobs"
        )


        top_three = results[:3]


        for i, result in enumerate(
            top_three,
            start=1
        ):

            st.write(
                f"### {i}. {result['Job Role']}"
            )

            st.progress(
                min(
                    result["Match Score"] / 100,
                    1.0
                )
            )

            st.write(
                f"Match Score: **{result['Match Score']}%**"
            )


        # ==================================================
        # SKILL GAP ANALYSIS
        # ==================================================

        st.header(
            "🎯 Skill Gap Analysis"
        )


        # Read job roles CSV

        job_roles = pd.read_csv(
            "data/job_roles.csv"
        )


        # ==================================================
        # SELECT TARGET JOB ROLE
        # ==================================================

        selected_role = st.selectbox(
            "Select a target job role",
            job_roles["Job Role"].tolist()
        )


        # ==================================================
        # GET SELECTED JOB
        # ==================================================

        selected_job = job_roles[
            job_roles["Job Role"] == selected_role
        ].iloc[0]


        # ==================================================
        # REQUIRED SKILLS
        # ==================================================

        required_skills = [
            skill.strip()
            for skill in selected_job[
                "Required Skills"
            ].split(",")
        ]


        # ==================================================
        # FIND MISSING SKILLS
        # ==================================================

        missing_skills = find_missing_skills(
            found_skills,
            required_skills
        )


        # ==================================================
        # FIND SKILLS FOR TARGET ROLE
        # ==================================================

        found_skills_lower = [
            skill.lower()
            for skill in found_skills
        ]


        target_found_skills = []

        for skill in required_skills:

            if skill.lower() in found_skills_lower:

                target_found_skills.append(
                    skill
                )


        # ==================================================
        # DISPLAY TARGET ROLE SKILLS
        # ==================================================

        st.subheader(
            f"Skills for {selected_role}"
        )


        # ==================================================
        # SKILLS FOUND
        # ==================================================

        if target_found_skills:

            st.write(
                "### ✅ Skills Found"
            )

            for skill in target_found_skills:

                st.write(
                    f"✓ {skill}"
                )

        else:

            st.write(
                "No required skills found for this role."
            )


        # ==================================================
        # MISSING SKILLS
        # ==================================================

        if missing_skills:

            st.write(
                "### ❌ Missing Skills"
            )

            for skill in missing_skills:

                st.write(
                    f"✗ {skill}"
                )

        else:

            st.success(
                "Great! No required skills are missing."
            )


        # ==================================================
        # LEARNING ROADMAP
        # ==================================================

        st.header(
            "📚 Learning Roadmap"
        )


        roadmap = generate_roadmap(
            missing_skills
        )


        if roadmap:

            for i, topic in enumerate(
                roadmap,
                start=1
            ):

                st.write(
                    f"**Week {i}:** {topic}"
                )

        else:

            st.success(
                "No additional learning topics are required."
            )


        # ==================================================
        # DOWNLOAD ANALYSIS REPORT
        # ==================================================

        st.header(
            "📥 Download Analysis Report"
        )


        # Create report

        report = f"""
AI RESUME ANALYZER & JOB RECOMMENDATION SYSTEM
==============================================

RESUME
------
{uploaded_file.name}


SKILLS FOUND
------------
"""


        # Add skills

        for skill in found_skills:

            report += f"✓ {skill}\n"


        # Add Top 3 jobs

        report += """

TOP 3 RECOMMENDED JOBS
----------------------
"""


        for i, result in enumerate(
            top_three,
            start=1
        ):

            report += (
                f"{i}. {result['Job Role']} - "
                f"{result['Match Score']}%\n"
            )


        # Add target role

        report += f"""

TARGET JOB ROLE
---------------
{selected_role}


SKILLS FOUND FOR TARGET ROLE
----------------------------
"""


        for skill in target_found_skills:

            report += f"✓ {skill}\n"


        # Add missing skills

        report += """

MISSING SKILLS
--------------
"""


        if missing_skills:

            for skill in missing_skills:

                report += f"✗ {skill}\n"

        else:

            report += (
                "No missing skills.\n"
            )


        # Add roadmap

        report += """

LEARNING ROADMAP
----------------
"""


        if roadmap:

            for i, topic in enumerate(
                roadmap,
                start=1
            ):

                report += (
                    f"{i}. {topic}\n"
                )

        else:

            report += (
                "No additional learning topics required.\n"
            )


        # Footer

        report += """

==============================================
Generated by AI Resume Analyzer
"""


        # ==================================================
        # DOWNLOAD BUTTON
        # ==================================================

        st.download_button(
            label="📥 Download Analysis Report",
            data=report,
            file_name="AI_Resume_Analysis_Report.txt",
            mime="text/plain"
        )


        # ==================================================
        # VIEW EXTRACTED RESUME TEXT
        # ==================================================

        with st.expander(
            "📄 View Extracted Resume Text"
        ):

            st.text(
                resume_text
            )