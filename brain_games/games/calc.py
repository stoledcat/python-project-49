import random
import operator
import prompt
from brain_games.cli import welcome_user


def calculation():
    user_name = welcome_user()
    print('What is the result of the expression?')
    seq = ((operator.add, '+'), (operator.sub, '-'), (operator.mul, '*'))
    count = 0
    for i in range(3):
        number1, number2 = random.randint(1, 10), random.randint(1, 10)
        operand, sign = random.choice(seq)
        print('Question: ', number1, sign, number2)
        user_answer = prompt.string('Your answer: ')
        right_answer = str(operand(number1, number2))
        if user_answer == str(right_answer):
            print('Correct!')
            count += 1
            if count == 3:
                print(f"Congratulations, {user_name}!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break
