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

    def pay(self, price):
        if self.__balance > price:
            self.__balance -= price
            return True
        else:
            return False

    def sell(self, price):
        self.__balance += price
