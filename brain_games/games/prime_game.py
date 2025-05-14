from random import randint

from prompt import string


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    random_number = randint(2, 9)
    question = str(random_number)
    answer = 'yes'
    for i in range(2, int(random_number ** 0.5) + 1):
        if random_number % i == 0:
            answer = 'no'
    return question, answer


