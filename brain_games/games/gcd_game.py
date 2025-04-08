from random import randint
from prompt import string

import math


def question_gcd():
    print('Find the greatest common divisor of given numbers.')


def gcd():
    random_number_1 = randint(1, 9)
    random_number_2 = randint(1, 9)
    print(f"Question: {random_number_1} {random_number_2}")
    user_answer = string("Your answer: ")
    answer = math.gcd(random_number_1, random_number_2)
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