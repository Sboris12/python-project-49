from prompt import string

ROUNDS_COUNT = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.GET_RULES)
    for i in range(ROUNDS_COUNT):
        question, answer = game.generate_round_data()
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




