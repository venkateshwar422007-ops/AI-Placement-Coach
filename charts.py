import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def generate_chart(role_scores):

    roles = list(role_scores.keys())
    scores = list(role_scores.values())

    plt.figure(figsize=(8, 5))
    plt.bar(roles, scores)

    plt.title("Role Match Scores")
    plt.ylabel("Match Percentage")

    plt.tight_layout()

    plt.savefig("static/chart.png")

    plt.close()