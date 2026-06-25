from flask import Flask, render_template
import json

from utils.parser import extract_text
from utils.skills import extract_skills
from utils.scorer import calculate_score

app = Flask(__name__)

@app.route('/')
def home():

    resume_path = "resume.txt"

    text = extract_text(resume_path)
    user_skills = extract_skills(text)

    with open("data/job_roles.json", "r") as file:
        roles = json.load(file)

    best_role = None
    best_score = 0
    missing_skills = []
    role_scores = {}

    for role, role_skills in roles.items():

        score = calculate_score(user_skills, role_skills)

        role_scores[role] = score

        if score > best_score:
            best_score = score
            best_role = role
            missing_skills = list(
                set(role_skills) - set(user_skills)
            )

    return render_template(
        "index.html",
        skills=user_skills,
        scores=role_scores,
        best_role=best_role,
        best_score=best_score,
        missing_skills=missing_skills
    )

if __name__ == "__main__":
    app.run(debug=True)