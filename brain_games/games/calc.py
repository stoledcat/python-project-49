# #!/usr/bin/env python3
import random
from operator import add, sub, mul
import prompt
from brain_games.cli import user_name


def calculation():
    print('What is the result of the expression?')
    ops = (add, sub, mul)
    oper = ''
    count = 0
    for i in range(3):
        number1, number2 = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(ops)
        if op == add:
            oper = '+'
        elif op == sub:
            oper = '-'
        elif op == mul:
            oper = '*'
        print('Question: ', number1, oper, number2)
        user_answer = prompt.string('Your answer: ')
        right_answer = op(number1, number2)
        if int(user_answer) == right_answer:
            print('Correct!')
            count += 1
            if count == 3:
                print(f"Congratulations, {user_name}!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break
