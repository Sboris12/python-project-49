from random import randint


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    random_number = randint(2, 9)
    question = str(random_number)
    answer = 'yes'
    for i in range(2, int(random_number ** 0.5) + 1):
        if random_number % i == 0:
            answer = 'no'
    return question, answer


