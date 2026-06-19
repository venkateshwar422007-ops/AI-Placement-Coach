def extract_skills(text):

    skills_database = [

        # Programming
        "python",
        "java",
        "c",
        "c++",
        "javascript",
        "html",
        "css",

        # Databases
        "sql",
        "mysql",
        "mongodb",

        # Data Science
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "statistics",

        # Machine Learning
        "machine learning",
        "deep learning",
        "tensorflow",
        "keras",
        "scikit-learn",
        "opencv",

        # Development
        "flask",
        "django",
        "react",
        "node.js",
        "git",
        "github",

        # Core CS
        "data structures",
        "algorithms",
        "dbms",
        "operating system",
        "computer networks",
        "oop",
        "oops",

        # Cloud
        "aws",
        "azure",
        "gcp",

        # Analytics
        "power bi",
        "excel",
        "tableau",

        # AI
        "artificial intelligence",
        "nlp",
        "generative ai",
        "llm",

        # Others
        "linux",
        "docker",
        "api",
        "rest api"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_database:

        if skill in text:
            found_skills.append(skill)

    return found_skills