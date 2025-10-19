import random

from brain_games.game import run_game

MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    question = random.randint(0, MAX_NUMBER)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer


def run_even_game():
    run_game(DESCRIPTION, generate_round)
