import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(number):
    divider = 2
    while divider < number:
        if number % divider == 0:
            return False
        divider += 1
    return True


def start_function():
    random_num = random.randint(2, 10)
    question = random_num
    if check_prime(random_num):
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer
