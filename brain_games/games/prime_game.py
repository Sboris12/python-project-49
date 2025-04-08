from random import randint

from prompt import string


def question_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime():
    random_number = randint(2, 9)
    answer = 'yes'
    for i in range(2, int(random_number ** 0.5) + 1):
        if random_number % i == 0:
            answer = 'no'
    print(f"Question: {random_number}")
    user_answer = string("Your answer: ")
    if answer == 'yes' and user_answer == "yes":
        return True, answer, user_answer
    elif answer == 'no' and user_answer == "no":
        return True, answer, user_answer
    else:
        return False, answer, user_answer