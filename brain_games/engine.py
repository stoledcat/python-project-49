import prompt

ROUNDS = 3
WIN_COUNT = 0


def repeated_code(task):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(task.DESCRIPTION)
    while WIN_COUNT < ROUNDS:
        question, right_answer = task.game_task()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
            WIN_COUNT += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.' \
Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break
    if WIN_COUNT == 3:
        print(f'Congratulations, {user_name}!')
