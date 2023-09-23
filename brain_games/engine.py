import prompt


def repeated_code(task):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(task.description)
    win_count = 0
    rounds = 3
    while win_count < rounds:
        question, right_answer = task.game_task()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
            win_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.' \
Correct answer was '{right_answer}'")
            print(f"Let's try again, {user_name}!")
            break
    if win_count == 3:
        print(f'Congratulations, {user_name}!')