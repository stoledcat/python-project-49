import random
import prompt
from brain_games.cli import welcome_user


def progression():
    user_name = welcome_user()
    count = 0
    # генерация трех чисел указана с 2, чтобы в итоговом ряду было 5+ элементов
    print('What number is missing in the progression?')

    for k in range(3):
        num1, num2, num3 = (random.randint(2, 10) for i in range(3))
        num2 = (num1 + num2 + num3)  # гарантированное увеличение STOP для range
        print('Question: ', end='')
        for i in range(num1, num2):  # генерация числового ряда
            print(num1, end=' ')
            if i == num2 - num3:        # сравнение счетчика с рандомным числом
                print('..', end=' ')    # для замены числа в ряду на '..'
                num1 += num3            # сдвиг следующего числа в ряду на шаг
                hidden_num = num1
            num1 += num3
        answer = prompt.string('\nYour answer: ')
        if answer.isdigit() and int(answer) == hidden_num:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \
                Correct answer was '{hidden_num}'.")
            print(f"Let's try again, {user_name}!")
            break
        if count == 3:
            print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    progression()
