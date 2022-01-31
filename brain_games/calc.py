import random
import prompt

number = random.randint(1, 100)
number1 = random.randint(1, 100)
actions = ('+', '-', '*')
action = random.choice(actions)
question = f"{number} {action} {number1}"


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


def quest():
    """ global number
    number = random.randint(1, 100)
    number1 = random.randint(1, 100)
    actions = ('+', '-', '*')
    action = random.choice(actions)
    global question
    # question = '{} {} {}'.format(number, action, number1)
    question = f"{number} {action} {number1}" """
    print('Question: ', question)
    global answ
    answ = input('Your answer: ')


def check_answer():
    win_count = 0
    while win_count < 3:
        quest()
        if answ == question:
            print('Correct!')
            win_count += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answ, question))
            print("Let's try again, {}!".format(name))
            break
    if win_count == 3:
        print('Congrulations, {}!'.format(name))
