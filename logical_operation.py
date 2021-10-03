# Grade judgment program using logical product(AND operation).
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


# Both Y and y are judged as "yes" by the logical sum(OR operation).
def func_or():
    a = input('Do you like a dog? (Y/N)...')  # Display a message prompting you to enter a key.

    if (a == 'Y') or (a == 'y'):  # When "Y" or "y" is entered.
        print('Yes')
    else:
        print('No')
