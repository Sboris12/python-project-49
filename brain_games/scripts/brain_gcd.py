from brain_games.games.gcd_game import gcd, get_rules
from brain_games.games.start import games


def main():
    games(gcd, get_rules)


if __name__ == "__main__":
    main()