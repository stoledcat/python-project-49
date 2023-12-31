import math
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def start_function():
    a, b = random.randint(40, 100), random.randint(40, 100)
    question = f'Question: {a} {b}'
    right_answer = str(math.gcd(a, b))
    return question, right_answer
