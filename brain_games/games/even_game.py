from random import randint

GET_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round_data():
    random_number = randint(1, 9)
    question = str(random_number)
    if random_number % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    return question, answer

