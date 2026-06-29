def final_score(
    semantic,
    skill_match,
    experience
):

    score = (
        semantic * 0.5 +
        skill_match * 0.3 +
        experience * 0.2
    )

    return round(score * 100, 2)
