from random import randint

from prompt import string


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    random_number = randint(1, 9)
    question = str(random_number)
    if random_number % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return question, answer

