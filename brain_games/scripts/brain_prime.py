from brain_games.games.prime_game import get_rules, prime
from brain_games.games.start import games


def main():
    games(prime, get_rules)


if __name__ == "__main__":
    main()