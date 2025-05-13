from brain_games.games.prime_game import prime, get_rules
from brain_games.games.start import games


def main():
    games(prime, get_rules)


if __name__ == "__main__":
    main()