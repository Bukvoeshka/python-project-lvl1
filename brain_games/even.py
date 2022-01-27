from os import name
import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    # print('Hello, ' + name + '!')
    print('Hello, {}!'.format(name))


def quest():
    global number
    number = random.randint(1, 100)
    print('Question: {}'.format(number))
    global answ
    answ = input('Your answer: ')


def check_answer():
    if number % 2 == 0 and answ == 'yes':
        print('Correct!')
    elif number % 2 == 0 and answ != 'yes':
        print("'{}' is wrong answer ;(. Correct answer was 'yes'.".format(answ))
        print("Let's try again, {}!".format(name))
    elif number % 2 != 0 and answ == 'no':
        print('Correct!')
    elif number % 2 != 0 and answ != 'no':
        print("'{}' is wrong answer ;(. Correct answer was 'no'.".format(answ))
        print("Let's try again, {}!".format(name))
