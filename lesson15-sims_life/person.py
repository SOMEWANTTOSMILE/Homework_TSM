from random import randint
from cars import Car
from bank import BankAccount


class Person:
    def __init__(self, name):
        self.name = name
        self.bank_account = BankAccount()
        self.car = None
        self.house = None

    def __str__(self):
        return f"Name - {self.name}, money - {self.bank_account}, car - {self.car}, house - {self.house}"

    def work(self):
        salary = randint(5, 10)
        self.bank_account.add_money(salary)

    def buy_car(self, car):
        if self.bank_account.pay(car.car_price):
            self.car = car
            return self.car
        return False

    def sell_car(self, car):
        self.bank_account.sell(car.car_price)
        self.car = None

    def buy_house(self, house):
        if self.car is not None and self.bank_account.pay(house.house_price):
            self.house = house
            return self.house
        return False

    def sell_house(self, house):
        self.bank_account.sell(house.house_price)
        self.house = None
