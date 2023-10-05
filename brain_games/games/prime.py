import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_random_num():
    random_num = random.randint(2, 101)
    return random_num


def start_function():
    random_num = generate_random_num()
    divider = 2
    while divider < random_num:
        if random_num % divider == 0:
            return False
        divider += 1
    return True
