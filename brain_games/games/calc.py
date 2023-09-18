from operator import add, sub, mul
from random import randint, choice
import prompt
from brain_games.cli import welcome_user


def calculation():
    user_name = welcome_user()
    print('What is the result of the expression?')
    operations = ((add, '+'), (sub, '-'), (mul, '*'))
    count = 0
    for i in range(3):
        number1, number2 = randint(1, 10), randint(1, 10)
        operator, sign = choice(operations)
        print(f'Question: {number1} {sign} {number2}')
        user_answer = prompt.string('Your answer: ')
        right_answer = str(operator(number1, number2))
        if user_answer == str(right_answer):
            print('Correct!')
            count += 1
            if count == 3:
                print(f"Congratulations, {user_name}!")
        else:
            print(f"'{user_answer}' is wrong answer ;(.' \
                Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break
