from random import randint
from cars import Dealer, Car
from bank import BankAccount


class Person:
    def __init__(self, name):
        self.name = name
        self.bank_account = BankAccount()
        self.car = list()
        self.house = list()

    def __str__(self):
        return f"Name - {self.name}, money - {self.bank_account}, car - {self.car}, house - {self.house}"

    def work(self):
        salary = randint(5, 10)
        self.bank_account.add_money(salary)

    def byu_car(self):
        pass

    def sell_car(self):
        pass

    def buy_house(self):
        pass

    def sell_house(self):
        pass
