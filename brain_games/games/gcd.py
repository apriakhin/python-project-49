import random

from brain_games.game import run_game

MAX_NUMBER = 100
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_round():
    a = random.randint(0, MAX_NUMBER)
    b = random.randint(0, MAX_NUMBER)
    question = f"{a} {b}"
    correct_answer = f"{gcd(a, b)}"
    return question, correct_answer


def run_gcd_game():
    run_game(DESCRIPTION, generate_round)
