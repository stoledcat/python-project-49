import random


DESCRIPTION = 'What number is missing in the progression?'


def generate_question():
    start_number, stop_number, step = (random.randint(2, 30) for i in range(3))
    stop_number = (start_number + stop_number + step) * 4
    question = list(range(start_number, stop_number, step))
    return question


def start_function():
    question = generate_question()
    len_question = len(question)
    index_answer = random.choice(range(0, len_question))
    right_answer = question[index_answer]
    question[index_answer] = '..'
    question = ' '.join(map(str, question))
    return question, str(right_answer)
