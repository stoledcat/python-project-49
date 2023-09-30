import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_task():
    number = random.randint(1, 100)
    question = number
    right_answer = 'yes' if (number % 2) == 0 else 'no'
    return question, right_answer
