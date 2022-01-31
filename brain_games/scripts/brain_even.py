from brain_games.even import welcome_user
from brain_games.even import check_answer


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    check_answer()


if __name__ == '__main__':
    main()
