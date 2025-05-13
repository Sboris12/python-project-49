from brain_games.games.even_game import even, get_rules
from brain_games.games.start import games


def main():
    games(even, get_rules)


if __name__ == "__main__":
    main()
