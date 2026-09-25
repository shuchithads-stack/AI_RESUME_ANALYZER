from job_matcher import calculate_match_score


resume = """
Python, Pandas, NumPy, Machine Learning,
Scikit-learn, SQL and Data Analysis
"""

job = """
Python, Pandas, NumPy, Machine Learning,
Scikit-learn, SQL, Data Analysis and Power BI
"""

score = calculate_match_score(resume, job)

print("Resume Match Score:", score, "%")