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
        question, answer= game()
        print(f"Question: {question}")
        user_answer = string("Your answer: ")
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'."
                  f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            if i == 2:
                win(name)


def win(name):
    print(f'Congratulations, {name}!.')



