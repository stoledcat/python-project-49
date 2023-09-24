import random


description = 'What number is missing in the progression?'


def game_task():
    # генерация трех чисел указана с 2, чтобы в итоговом ряду было 5+ элементов
    start_number, stop_number, step = (random.randint(2, 30) for i in range(3))
    # гарантированное увеличение STOP для range
    stop_number = (start_number + stop_number * step)
    # создние арифметической прогрессии
    progression = list(range(start_number, stop_number, step))
    right_answer = random.choice(progression)
    question = '' + ' '.join(
        '..' if num == right_answer else str(num) for num in progression
    )
    return question, str(right_answer)
