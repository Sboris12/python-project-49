from random import randint

from prompt import string


def question_progression():
    print('What number is missing in the progression?')


def progression():
    start = randint(1, 9)
    step = randint(1, 9)
    invisible = randint(0, 9)
    prog = [start + step * i for i in range(10)]
    answer = prog[invisible]
    prog[invisible] = '..'
    question = ' '.join(str(x) for x in prog)
    print(f"Question: {question}")
    user_answer = string("Your answer: ")
    while True:
        try:
            good_user_answer = int(user_answer)
            break
        except ValueError:
            return False, answer, user_answer
    if answer == good_user_answer:
        return True, answer, user_answer
    else:
        return False, answer, user_answer

