from skill_extractor import extract_skills, find_missing_skills


resume = """
I have experience in Python, Pandas, NumPy,
Machine Learning and Scikit-learn.
I also know SQL and Deep Learning.
"""


# Extract skills from resume
found_skills = extract_skills(resume)


# Required skills for AI Engineer
required_skills = [
    "Python",
    "Deep Learning",
    "LLM",
    "RAG",
    "APIs"
]


# Find missing skills
missing_skills = find_missing_skills(
    found_skills,
    required_skills
)


print("\nSKILLS FOUND")
print("============")

for skill in found_skills:
    print("✓", skill)


print("\nMISSING SKILLS")
print("==============")

for skill in missing_skills:
    print("✗", skill)