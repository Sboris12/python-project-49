from random import randint

from prompt import string


def get_rules():
    return 'What number is missing in the progression?'


def progression():
    start = randint(1, 9)
    step = randint(1, 9)
    invisible = randint(0, 9)
    prog = [start + step * i for i in range(10)]
    answer = str(prog[invisible])
    prog[invisible] = '..'
    question = str(' '.join(str(x) for x in prog))
    return question, answer


