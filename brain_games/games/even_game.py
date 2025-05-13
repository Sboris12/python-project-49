from random import randint

from prompt import string


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    random_number = randint(1, 9)
    print(f"Question: {random_number}")
    if random_number % 2 == 0:
        answer = "yes"
    else:
        answer = "no"
    user_answer = string("Your answer: ")
    if random_number % 2 == 0 and user_answer == "yes":
        return True, answer, user_answer
    elif random_number % 2 != 0 and user_answer == "no":
        return True, answer, user_answer
    else:
        return False, answer, user_answer

