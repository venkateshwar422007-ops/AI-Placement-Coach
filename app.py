from flask import Flask, render_template, request
import json
import os

from utils.parser import extract_text
from utils.skills import extract_skills
from utils.scorer import calculate_score
from charts import generate_chart

app = Flask(__name__)

# Upload folder setup
UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    best_role = None
    best_score = 0
    user_skills = []
    missing_skills = []
    role_scores = {}

    if request.method == "POST":

        uploaded_file = request.files["resume"]

        if uploaded_file and uploaded_file.filename != "":

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                uploaded_file.filename
            )

            uploaded_file.save(filepath)

            text = extract_text(filepath)

            user_skills = extract_skills(text)

            with open("data/job_roles.json", "r") as file:
                roles = json.load(file)

            for role, role_skills in roles.items():

                score = calculate_score(
                    user_skills,
                    role_skills
                )

                role_scores[role] = score

                if score > best_score:
                    best_score = score
                    best_role = role

                    missing_skills = list(
                        set(role_skills) - set(user_skills)
                    )

            # Generate chart
            generate_chart(role_scores)

    return render_template(
        "index.html",
        best_role=best_role,
        best_score=best_score,
        skills=user_skills,
        missing_skills=missing_skills,
        scores=role_scores
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
