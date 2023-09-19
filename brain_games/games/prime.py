import random
import prompt
from brain_games.cli import welcome_user


def prime_check(random_num):
    divider = 2
    while random_num % divider != 0:
        divider += 1
    if divider == random_num:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer


def is_prime():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_answers = 0
    for answers in range(3):
        random_num = random.randint(2, 101)
        right_answer = prime_check(random_num)
        print('Question:', random_num)
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            count_answers += 1
            if count_answers == 3:
                print(f"Congratulations, {user_name}!")
        else:
            print(f"Wrong answer. Let's try again, {user_name}!")
            break
