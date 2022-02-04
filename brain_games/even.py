import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def quest():
    global number
    number = random.randint(1, 100)
    print(f'Question: {number}')
    global answ
    answ = input('Your answer: ')


def check_answer():
    win_count = 0
    while win_count < 3:
        quest()
        if number % 2 == 0 and answ == 'yes' or number % 2 != 0 and answ == 'no':
            print('Correct!')
            win_count += 1
        elif number % 2 == 0 and answ != 'yes':
            print(f"'{answ}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif number % 2 != 0 and answ != 'no':
            print(f"'{answ}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    if win_count == 3:
        print(f'Congrulations, {name}!')
