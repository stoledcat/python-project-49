import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def start_function():
    number = random.randint(1, 100)
    question = number
    right_answer = 'yes' if (number % 2) == 0 else 'no'
    return question, right_answer
