import random


description = 'What number is missing in the progression?'


def game_task():
    # генерация трех чисел указана с 2, чтобы в итоговом ряду было 5+ элементов
    start_number, stop_number, step = (random.randint(2, 10) for i in range(3))
    # гарантированное увеличение STOP для range
    stop_number = (start_number + stop_number + step)
    # print('Question: ', end='')
    for i in range(start_number, stop_number):  # генерация числового ряда
        print(start_number, end=' ')
        # сравнение счетчика с рандомным числом
        # для замены этого числа в ряду на '..'
        if i == stop_number - step:
            print('..', end=' ')
            # сдвиг следующего числа в ряду на шаг
            start_number += step
            right_answer = start_number
        start_number += step
        question = start_number
    return question, str(right_answer)
