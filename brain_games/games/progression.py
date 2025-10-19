import random

from brain_games.game import run_game

MAX_START = 20
MIN_STEP = 1
MAX_STEP = 5
MIN_COUNT = 5
MAX_COUNT = 10
DESCRIPTION = 'What number is missing in the progression?'


def generate_arithmetic_sequence(start, step, count):
    return [str(start + step * i) for i in range(count)]


def generate_round():
    start = random.randint(0, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    count = random.randint(MIN_COUNT, MAX_COUNT)
    elements = generate_arithmetic_sequence(start, step, count)
    answer_index = random.randint(0, count - 1)
    correct_answer = f"{elements[answer_index]}"
    elements[answer_index] = '..'
    question = ' '.join(elements)
    return question, correct_answer


def run_progression_game():
    run_game(DESCRIPTION, generate_round)
