from brain_games.games.progression_game import get_rules, progression
from brain_games.games.start import games


def main():
    games(progression, get_rules)


if __name__ == "__main__":
    main()