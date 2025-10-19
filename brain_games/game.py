import prompt

ROUNDS_COUNT = 3


def run_game(description, generate_round):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(description)

    rounds = []
    for _ in range(ROUNDS_COUNT):
        rounds.append(generate_round())

    for question, correct_answer in rounds:
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        
        if answer == correct_answer:
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
