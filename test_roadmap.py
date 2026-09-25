from roadmap_generator import generate_roadmap


missing_skills = [
    "LLM",
    "RAG",
    "APIs"
]


roadmap = generate_roadmap(missing_skills)


print("\nLEARNING ROADMAP")
print("================")

for i, topic in enumerate(roadmap, start=1):

    print(f"{i}. {topic}")