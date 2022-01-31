#!/usr/bin/env python

from brain_games.calc import welcome_user
from brain_games.calc import check_answer


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('What is the result of the expression?')
    check_answer()


if __name__ == '__main__':
    main()
