from random import choice, randint

from prompt import string


def get_rules():
    return 'What is the result of the expression?'


def calc():
    operators = ['+', '-', '*']
    random_number_1 = randint(1, 9)
    random_number_2 = randint(1, 9)
    random_operator = choice(operators)
    answer = eval(f'{random_number_1}{random_operator}{random_number_2}')
    print(f"Question: {random_number_1} {random_operator} {random_number_2}")
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