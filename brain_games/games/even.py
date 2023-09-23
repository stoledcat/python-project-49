import random
# import prompt


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_task():
    pattern = ['0yes', '1no']
    number = random.randint(1, 100)
    # if str(number % 2) + user_answer in pattern:
    question = number
    right_answer = 'yes' if str(number % 2) + user_answer in pattern else 'no'
    return question, right_answer
