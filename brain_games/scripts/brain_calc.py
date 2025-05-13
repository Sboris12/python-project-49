from brain_games.games.calc_game import calc, get_rules
from brain_games.games.start import games


def main():
    games(calc, get_rules)


if __name__ == "__main__":
    main()