from random import choice, randint

GET_RULES = 'What is the result of the expression?'


def generate_round_data():
    operators = ['+', '-', '*']
    random_number_1 = randint(1, 9)
    random_number_2 = randint(1, 9)
    random_operator = choice(operators)
    question = f"{random_number_1} {random_operator} {random_number_2}"
    answer = str(eval(f'{random_number_1}{random_operator}{random_number_2}'))
    return question, answer
