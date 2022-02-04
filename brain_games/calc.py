import random
import prompt


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


# узнать насчёт способов облегчить функцию
def quest():
    global number1
    global number2
    global operation
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = f'{number1} {operation} {number2}'
    print('Question: ', question)


def resl():
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2


def check_answer():
    win_count = 0
    while win_count < 3:
        quest()
        answ = input('Your answer: ')
        if answ == str(resl()):
            print('Correct!')
            win_count += 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{str(resl())}'.")
            print(f"Let's try again, {name}!")
            break
    if win_count == 3:
        print(f'Congratulations, {name}!')
