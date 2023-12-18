class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    def __repr__(self):
        return f"{self.balance}"

    def add_money(self, salary):
        self.__balance += salary
