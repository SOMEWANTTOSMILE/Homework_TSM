from functions import summ, subtraction, multiplication, division, exponentiation
from custom_except import WrongOption, WrongValue


def get_user_number():
    user_data = list()
    try:
        while len(user_data) != 2:
            number = (input("Enter number: "))
            if not number.isdigit():
                raise WrongValue
            else:
                user_data.append(number)
    except WrongValue:
        print("Please, enter number")
        return get_user_number()
    return int(user_data[0]), int(user_data[1])


def get_operation():
    try:
        operation = input("what operation do you want to perform?(+, -, *, /, **): ")
        if not operation in ["+", "-", "*", "/", "**"]:
            raise WrongOption
        else:
            return operation
    except WrongOption:
        print("please enter one of the following operations(+, -, *, /, **)")
        return get_operation()


def calc():
    numbers = get_user_number()
    operation = get_operation()
    first_number, second_number = numbers[0], numbers[1]
    if operation == "+":
        return summ(first_number, second_number)
    if operation == "-":
        return subtraction(first_number, second_number)
    if operation == "*":
        return multiplication(first_number, second_number)
    if operation == "/":
        return division(first_number, second_number)
    if operation == "**":
        return exponentiation(first_number, second_number)


print(calc())
