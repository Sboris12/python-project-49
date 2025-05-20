from prompt import string

rounds = 3


def games(game):
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.get_rules())
    for i in range(rounds):
        question, answer = game.game_logic()
        print(f"Question: {question}")
        user_answer = string("Your answer: ")
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'."
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!.')




