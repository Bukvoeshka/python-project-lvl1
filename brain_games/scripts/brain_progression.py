#!/usr/bin/env python

from brain_games.progression import welcome_user
from brain_games.progression import check_answer


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('What number is missing in the progression?')
    check_answer()


if __name__ == '__main__':
    main()
