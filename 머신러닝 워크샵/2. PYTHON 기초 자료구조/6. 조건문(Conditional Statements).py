def exercise(score):
    # 1

    if score < 50:
        evaluation="Below average"

    elif 50 <=score< 70:
        evaluation= "Average"

    elif 70 <=score< 90:
        evaluation= "Above average"

    elif score >= 90:
        evaluation = "Excellent"

    return evaluation

print(exercise(80))
