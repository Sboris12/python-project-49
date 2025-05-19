from prompt import string


def games(game, rules_func):
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")
    print(rules_func())
    for i in range(3):
        question, answer = game()
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
                print(f'Congratulations, {name}!.')




