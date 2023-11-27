import json

with open('user_data.json', 'r') as json_file:
    user_data = json.load(json_file)


def get_gmail():
    return input('Enter your email:\n')


def get_password():
    return input('Enter your password:\n')


def password_confirmation():
    first_password = get_password()
    second_password = input('Confirm your password:\n')
    while True:
        if first_password == second_password:
            return second_password
        else:
            print("It seems you've entered incorrect data. Try again!")
            first_password = get_password()
            second_password = input('Confirm your password:\n')


def check_user_data():
    while True:
        name = get_gmail()
        for users in user_data:
            if users['email'] == name:
                print('This name is already used')
                break
        else:
            return name


def login():
    while True:
        email, password = get_gmail(), get_password()
        for users in user_data:
            if users['email'] == email and users['password'] == password:
                return f'Hello {email}'
        else:
            print("The password or email was entered incorrectly")


def registration():
    while True:
        name = check_user_data()
        password = password_confirmation()
        if name and password:
            new_user = {'email': name, 'password': password}
            user_data.append(new_user)
            with open('user_data.json', 'w') as file:
                json.dump(user_data, file)
            return 'Registration is over.'
        else:
            print("It seems you've entered something wrong. Try again!")


def login_register():
    while True:
        user_choice = input('What would you like to do: register or login?\n')
        if user_choice == 'register':
            return registration()
        if user_choice == 'login':
            return login()
        else:
            print('You need to choose: to login or to register!')


print(login_register())

