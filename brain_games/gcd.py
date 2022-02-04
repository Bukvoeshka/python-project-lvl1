import prompt
import random


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def quest():
    global number1
    global number2
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print('Question: ', number1, number2)


def gcd1():
    global divider1
    global number1
    divider1 = []
    d = 2
    while number1 > 1:
        while number1 % d == 0:
            divider1.append(d)
            number1 = number1 // d
        d += 1
    return divider1


def gcd2():
    global divider2
    global number2
    divider2 = []
    d = 2
    while number2 > 1:
        while number2 % d == 0:
            divider2.append(d)
            number2 = number2 // d
        d += 1
    return divider2


def intersection():
    global store
    target, iterate = [divider1, divider2] if len(divider2) >= len(divider1) else [divider2, divider1]
    i = 0
    store = []
    while i < len(iterate):
        element = iterate[i]
        if element in target:
            store.append(element)
            target.remove(element)
        i += 1
    return store


def gcd():
    global store
    global resultat
    resultat = 1
    if store == []:
        return 1
    else:
        for i in store:
            resultat *= i
        return resultat


def check_answer():
    global resultat
    win_count = 0
    while win_count < 3:
        quest()
        gcd1()
        gcd2()
        intersection()
        gcd()
        answ = input('Your answer: ')
        if answ == str(resultat):
            print('Correct!')
            win_count += 1
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{resultat}'.")
            print(f"Let's try again, {name}!")
            break
    if win_count == 3:
        print(f'Congratulations, {name}!')
