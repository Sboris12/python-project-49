from prompt import string

from brain_games.games.calc_game import question_calc
from brain_games.games.even_game import question_even
from brain_games.games.gcd_game import question_gcd
from brain_games.games.prime_game import question_prime
from brain_games.games.progression_game import question_progression


def greet():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def games(game):
    greet()
    name = welcome_user()
    if game.__name__ == 'even':
        question_even()
    elif game.__name__ == 'calc':
        question_calc()
    elif game.__name__ == 'progression':
        question_progression()
    elif game.__name__ == 'prime':
        question_prime()
    else:
        question_gcd()

    for i in range(3):
        result, answer, user_answer = game()
        if not result:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
        else:
            print("Correct!")
    if result:
        win(name)


def win(name):
    print(f'Congratulations, {name}!.')

