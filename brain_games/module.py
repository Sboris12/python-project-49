from random import randint

from prompt import string


def greet():
    print("Welcome to the Brain Games!")


def welcome_user():
    global name
    name = string("May I have your name? ")
    print(f"Hello, {name}!")


def even(win=1, answer="", user_answer=""):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = randint(1, 9)
        print(f"Question: {random_number}")
        if random_number % 2 == 0:
            answer = "yes"
        else:
            answer = "no"
        user_answer = string("Your answer: ")
        if random_number % 2 == 0 and user_answer == "yes":
            print("Correct!")
        elif random_number % 2 != 0 and user_answer == "no":
            print("Correct!")
        else:
            win = 0
            break
    if win == 1:
        print(f"Congratulations, {name}!")
    else:
        print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{answer}'.\nLet's try again, {name}!"
        )
