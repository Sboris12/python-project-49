from prompt import string


def main():
    print("Welcome to the Brain Games!")
    name = string("May I have your name? ")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()