import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text, job_description):
    """
    Calculate similarity between resume text and job description
    using TF-IDF and cosine similarity.
    """

    # Make sure inputs are strings
    resume_text = str(resume_text)
    job_description = str(job_description)

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def recommend_jobs(resume_text, csv_path=None):

    # Get the folder where this Python file is located
    base_dir = Path(__file__).resolve().parent

    # Always use job_roles.csv from the project folder
    csv_file = base_dir / "job_roles.csv"

    # Read job data
    jobs = pd.read_csv(csv_file)

    results = []

    for _, row in jobs.iterrows():

        job_role = str(row["Job Role"])
        required_skills = str(row["Required Skills"])

        score = calculate_match_score(
            resume_text,
            required_skills
        )

        results.append({
            "Job Role": job_role,
            "Match Score": score
        })

    # Sort from highest score to lowest score
    results = sorted(
        results,
        key=lambda x: x["Match Score"],
        reverse=True
    )

    return results