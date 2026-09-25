from job_matcher import recommend_jobs


resume = """
Python, Pandas, NumPy, Machine Learning,
Scikit-learn, SQL, Data Analysis,
Deep Learning and Artificial Intelligence
"""


results = recommend_jobs(resume)


print("\nJOB RECOMMENDATIONS")
print("===================")

for i, result in enumerate(results, start=1):

    print(
        f"{i}. {result['Job Role']} - "
        f"{result['Match Score']}%"
    )


print("\nTOP 3 RECOMMENDED JOBS")
print("=======================")

for i, result in enumerate(results[:3], start=1):

    print(
        f"{i}. {result['Job Role']} - "
        f"{result['Match Score']}%"
    )