import random
import prompt
from brain_games.cli import user_name


def even():
    correct_answer = ['0yes', '1no']  # правильные ответы
    count = 0  # счетчик
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = random.randint(1, 100)
        print('Question:', number)  # выводится сгенерированное число
        answer = prompt.string('Your answer: ')  # ввод ответа yes/no
        if str(number % 2) + answer in correct_answer:  # сверяемся с ответами
            print('Correct!')
            count += 1
            if count == 3:
                print("Congratulations,", user_name + "!")
        else:
            print("Let's try again,", user_name + "!")
            break


if __name__ == '__main__':
    even()
