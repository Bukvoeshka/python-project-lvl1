#!/usr/bin/env python

from brain_games.gcd import welcome_user
from brain_games.gcd import check_answer


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Find the greatest common divisor of given numbers.')
    check_answer()


if __name__ == '__main__':
    main()
