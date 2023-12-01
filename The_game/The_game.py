import sys
from random import randint


def get_user_numbers():
    while True:
        user_data = set()
        for number in range(3):
            number = input('Enter number: ')
            if number == 'exit':
                sys.exit()
            else:
                user_data.add(int(number))
        if len(user_data) < 3:
            print("You cannot enter the same numbers")
        else:
            break
    return user_data


def get_range():
    while True:
        from_random = int(input("The range must contain at least 5 digits and no more than 30\nEnter range from: "))
        to_random = int(input("To... "))
        if 5 <= (to_random + 1) - from_random <= 30:
            break
        else:
            print('Wrong range')
    return from_random, to_random


def get_random_numbers():
    user_range = get_range()
    from_random, to_random = user_range[0], user_range[1]
    random_numbers = set()
    while len(random_numbers) < 3:
        random_number = randint(from_random, to_random)
        random_numbers.add(random_number)
    print(f'{random_numbers}')
    return random_numbers


def check_all():
    random_list_1 = get_random_numbers()
    while True:
        user_data = get_user_numbers()
        print(user_data)
        end_list = set(random_list_1).intersection(set(user_data))
        if len(end_list) == 3:
            print('You win!')
            break
        else:
            print(f'Try again, you guessed {len(end_list)} of numbers')


check_all()


