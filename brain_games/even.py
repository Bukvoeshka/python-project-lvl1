import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))


def quest():
    global number
    number = random.randint(1, 100)
    print('Question: {}'.format(number))
    global answ
    answ = input('Your answer: ')


def check_answer():
    win_count = 0
    while win_count < 3:
        quest()
        if number % 2 == 0 and answ == 'yes':
            print('Correct!')
            win_count += 1
        elif number % 2 == 0 and answ != 'yes':
            print("'{}' is wrong answer ;(. Correct answer was 'yes'.".format(answ))
            print("Let's try again, {}!".format(name))
            break
        elif number % 2 != 0 and answ == 'no':
            print('Correct!')
            win_count += 1
        elif number % 2 != 0 and answ != 'no':
            print("'{}' is wrong answer ;(. Correct answer was 'no'.".format(answ))
            print("Let's try again, {}!".format(name))
            break
    if win_count == 3:
        print('Congrulations, {}!'.format(name))
