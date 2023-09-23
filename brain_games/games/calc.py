from operator import add, sub, mul
from random import randint, choice

operations = ((add, '+'), (sub, '-'), (mul, '*'))
description = 'What is the result of the expression?'


def game_task():
    number1, number2 = randint(1, 10), randint(1, 10)
    operator, sign = choice(operations)
    right_answer = str(operator(number1, number2))
    question = f'{number1} {sign} {number2}'
    return question, right_answer
