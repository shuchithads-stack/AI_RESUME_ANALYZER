def generate_roadmap(missing_skills):

    roadmap = []

    learning_topics = {
        "Python": "Learn Python programming fundamentals",
        "SQL": "Learn SQL and database queries",
        "Excel": "Learn Excel data analysis",
        "Pandas": "Learn Pandas for data manipulation",
        "Power BI": "Learn Power BI and dashboard creation",
        "Machine Learning": "Learn Machine Learning fundamentals",
        "ML": "Learn Machine Learning fundamentals",
        "Scikit-learn": "Learn Scikit-learn for ML models",
        "FastAPI": "Learn FastAPI and API development",
        "Docker": "Learn Docker and containerization",
        "Deep Learning": "Learn Deep Learning and neural networks",
        "LLM": "Learn Large Language Model fundamentals",
        "RAG": "Learn Retrieval-Augmented Generation",
        "APIs": "Learn REST API development",
        "NLP": "Learn Natural Language Processing",
        "Transformers": "Learn Transformer models",
        "Hugging Face": "Learn Hugging Face Transformers",
        "OpenCV": "Learn OpenCV for computer vision",
        "CNN": "Learn Convolutional Neural Networks",
        "YOLO": "Learn YOLO object detection",
        "NumPy": "Learn NumPy for numerical computing"
    }

    for skill in missing_skills:

        topic = learning_topics.get(
            skill,
            f"Learn {skill}"
        )

        roadmap.append(topic)

    return roadmap