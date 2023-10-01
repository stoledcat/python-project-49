import random


DESCRIPTION = 'What number is missing in the progression?'


def start_function():
    start_number, stop_number, step = (random.randint(2, 30) for i in range(3))
    stop_number = (start_number + stop_number + step) * 4
    question = list(range(start_number, stop_number, step))
    len_question = len(question)
    index_answer = random.choice(range(0, len_question))
    right_answer = question[index_answer]
    question[index_answer] = '..'
    return question, str(right_answer)
