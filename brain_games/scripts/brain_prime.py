#!/usr/bin/env python

from brain_games.prime import check_answer, welcome_user


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    check_answer()


if __name__ == '__main__':
    main()
