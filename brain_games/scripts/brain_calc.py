from brain_games.games.calc_game import game, get_rules
from brain_games.start import games


def main():
    games(game, get_rules)


if __name__ == "__main__":
    main()