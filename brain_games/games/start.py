from prompt import string


def greet():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def games(game, rules_func):
    greet()
    name = welcome_user()
    print(rules_func())

    for i in range(3):
        result, answer, user_answer = game()
        if not result:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'."
                  f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
    if result:
        win(name)


def win(name):
    print(f'Congratulations, {name}!.')

