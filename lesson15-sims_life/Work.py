from random import randint
from bank import BankAccount


class Work:
    def __init__(self):
        self.salary = randint(5, 10)

    def work(self):
        BankAccount.add_money(self.salary)


