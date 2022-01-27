#!/usr/bin/env python

from brain_games.even import welcome_user
from brain_games.even import quest
from brain_games.even import check_answer


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    quest()
    check_answer()


if __name__ == '__main__':
    main()
