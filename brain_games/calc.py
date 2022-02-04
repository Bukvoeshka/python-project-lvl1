import random
import prompt


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


# узнать насчёт способов облегчить функцию
def quest():
    global number
    global number1
    global operation
    number = random.randint(1, 100)
    number1 = random.randint(1, 100)
    operation = random.choice(('+', '-', '*'))
    # question = f'{number} {operation} {number1}'
    print(f'Question: {number} {operation} {number1}')


def resl():
    if operation == '+':
        return number + number1
    elif operation == '-':
        return number - number1
    elif operation == '*':
        return number * number1


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
