from brain_games.games.progression_game import progression, get_rules
from brain_games.games.start import games


def main():
    games(progression, get_rules)


if __name__ == "__main__":
    main()