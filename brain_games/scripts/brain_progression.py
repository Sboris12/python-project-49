from brain_games.games.progression_game import get_rules, game
from brain_games.start import games


def main():
    games(game, get_rules)


if __name__ == "__main__":
    main()