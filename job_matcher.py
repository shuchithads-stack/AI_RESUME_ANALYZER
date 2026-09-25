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
    """
    Recommend jobs based on resume text.

    The job_roles.csv file is located in the same folder
    as this Python file.
    """

    # Find job_roles.csv relative to this Python file
    if csv_path is None:
        csv_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "job_roles.csv"
        )

    # Check whether the CSV file exists
    if not os.path.exists(csv_path):
        raise FileNotFoundError(
            f"job_roles.csv not found. Expected location: {csv_path}"
        )

    # Read job dataset
    jobs = pd.read_csv(csv_path)

    # Check required columns
    required_columns = ["Job Role", "Required Skills"]

    for column in required_columns:
        if column not in jobs.columns:
            raise ValueError(
                f"Missing required column: '{column}'. "
                f"Available columns: {list(jobs.columns)}"
            )

    results = []

    # Compare resume with every job
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