import random


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_task():
    random_num = random.randint(2, 101)
    question = random_num
    divider = 2
    while random_num % divider != 0:
        divider += 1
    if divider == random_num:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
