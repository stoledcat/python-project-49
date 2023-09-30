import random


DESCRIPTION = 'What number is missing in the progression?'


def start_function():
    start_number, stop_number, step = (random.randint(2, 30) for i in range(3))
    stop_number = (start_number + stop_number + step) * 5
    progression = list(range(start_number, stop_number, step))
    right_answer = random.choice(progression)
    question = '' + ' '.join(
        '..' if num == right_answer else str(num) for num in progression
    )
    return question, str(right_answer)
