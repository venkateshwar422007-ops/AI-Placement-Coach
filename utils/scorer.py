def calculate_score(user_skills, role_skills):

    matched = len(
        set(user_skills).intersection(set(role_skills))
    )

    score = (matched / len(role_skills)) * 100

    return round(score, 2)