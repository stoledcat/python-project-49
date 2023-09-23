import random
import prompt
from brain_games.cli import welcome_user


def is_even():
    user_name = welcome_user()
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
        else:
            print("Wrong answer. Let's try again,", user_name + "!")
            break
        print("Congratulations,", user_name + "!")
