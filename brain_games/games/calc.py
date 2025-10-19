import random

from brain_games.game import run_game

MAX_NUMBER = 100
OPERATIONS = ['+', '-', '*']
DESCRIPTION = 'What is the result of the expression?'


def calc(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b 
        case '*':
            return a * b
        case _:
            return None


def generate_round():
    a = random.randint(0, MAX_NUMBER)
    b = random.randint(0, MAX_NUMBER)
    random_index = random.randint(0, len(OPERATIONS) - 1)
    operation = OPERATIONS[random_index]
    question = f"{a} {operation} {b}"
    correct_answer = f"{calc(a, b, operation)}"
    return question, correct_answer


def run_calc_game():
    run_game(DESCRIPTION, generate_round)
