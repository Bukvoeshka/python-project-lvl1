import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def start():
    global progression
    step = random.randint(1, 9)
    element = random.randint(1, 9)
    lenght_progression = 10
    progression = [element]
    i = 1
    while i < lenght_progression:
        element += step
        progression.append(element)
        i += 1
    return progression


def middle():
    global rnd_elmnt
    num = random.randint(1, 9)
    rnd_elmnt = progression[num]
    progression[num] = '..'
    print('Question:', ' '.join(map(str, progression)))


def check_answer():
    win_count = 0
    while win_count < 3:
        start()
        middle()
        answ = input('Your answer: ')
        if answ == str(rnd_elmnt):
            print('Correct!')
            win_count += 1
            continue
        # else:
        print(f"'{answ}' is wrong answer ;(. Correct answer was '{rnd_elmnt}'.")
        print(f"Let's try again, {name}!")
        break
    if win_count == 3:
        print(f'Congratulations, {name}!')
