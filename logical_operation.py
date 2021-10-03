def func_and(score):
    if score >= 80:  # Score 80 points or more.
        rank = 'A'
    elif (score >= 60) and (score < 80):  # Score in the range of 60-79
        rank = 'B'
    elif (score >= 40) and (score < 60):  # Score in the range of 40-59
        rank = 'c'
    else:  # Other than the above(score is less than 40)
        rank = '追試'
    return rank
