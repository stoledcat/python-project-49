import random
import prompt
from brain_games.cli import user_name


def is_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_answers = 0                   # счетчик правильных ответов
    for answers in range(3):
        count_div = 0                   # счетчик делителей
        num = random.randint(2, 10)
        print('Question:', num)
        for i in range(2, num + 1):     # перебор делителей включая само число
            if (num % i) == 0:          # проверка на деление без остатка
                count_div += 1
        if count_div == 1:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:  # сравнение ответов
            print('Correct!')
            count_answers += 1
            if count_answers == 3:
                print(f"Congratulations, {user_name}!")
        else:
            print(f"Wrong answer. Let's try again, {user_name}!")
            break


if __name__ == '__main__':
    is_prime()
