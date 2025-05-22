import math
from random import randint

GET_RULES = 'Find the greatest common divisor of given numbers.'


def generate_round_data():
    random_number_1 = randint(1, 9)
    random_number_2 = randint(1, 9)
    question = f"{random_number_1} {random_number_2}"
    answer = str(math.gcd(random_number_1, random_number_2))
    return question, answer
