import math
import random
import prompt
from brain_games.cli import user_name


user_answer = 0
count = 0


def gcd_find():
    print('Find the greatest common divisor of given numbers.')
    count = 0
    for i in range(3):
        a, b = random.randint(40, 100), random.randint(40, 100)
        print('Question: ', a, b)
        user_answer = prompt.string('Your answer: ')
        right_answer = math.gcd(a, b)
        if int(user_answer) == right_answer:
            count += 1
            print('Correct!')
            if count == 3:
                print(f"Congratulations, {user_name}!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break


if __name__ == '__main__':
    gcd_find()
