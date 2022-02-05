import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def quest():
    global number
    number = random.randint(1, 100)
    print('Question:', number)
    global answ
    answ = input('Your answer: ')


def make_list():
    global list
    list = []
    d = 1
    while d <= number:
        if number % d == 0:
            list.append(d)
            d += 1
        else:
            d += 1
    return list


""" def check_answer():
    win_count = 0
    while win_count < 3:
        quest()
        ref_list = [1, number]
        make_list()
        if list == ref_list and answ == 'yes':
            print('Correct!')
            win_count += 1
        elif list != ref_list and answ == 'no':
            print('Correct!')
            win_count += 1
        elif list != ref_list and answ != 'no':
            print(f"'{answ}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        elif list == ref_list and answ != 'yes':
            print(f"'{answ}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
    if win_count == 3:
        print(f'Congratulations, {name}!') """


""" def check_answer():
    yes = f"'{answ}' is wrong answer ;(. Correct answer was 'yes'."
    no = f"'{answ}' is wrong answer ;(. Correct answer was 'no'."
    win_count = 0
    while win_count < 3:
        quest()
        ref_list = [1, number]
        make_list()
        if list == ref_list:
            if answ == 'yes':
                print('Correct!')
                win_count += 1
            else:
                print(yes)
                print(f"Let's try again, {name}!")
                break
        elif list != ref_list:
            if answ == 'no':
                print('Correct!')
                win_count += 1
            else:
                print(no)
                print(f"Let's try again, {name}!")
                break
    if win_count == 3:
        print(f'Congratulations, {name}!') """


def check_answer():
    win_count = 0
    while win_count < 3:
        quest()
        ref_list = [1, number]
        make_list()
        if list == ref_list and answ == 'yes':
            print('Correct!')
            win_count += 1
        elif list != ref_list and answ == 'no':
            print('Correct!')
            win_count += 1
        elif list != ref_list and answ != 'no':
            print(f"'{answ}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
    if win_count == 3:
        print(f'Congratulations, {name}!')
