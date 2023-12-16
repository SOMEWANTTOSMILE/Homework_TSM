from Bank_account import BankAccount


class Company:
    def __init__(self, name, profit, salary, legal_number):
        if profit <= salary:
            raise ValueError("This is bad company")

        self.name = name
        self.legal_number = legal_number
        self.__profit = profit
        self.__salary = salary
        self.__bank_account = BankAccount(f"{self.legal_number} - company")
        self.staff = set()

    def make_offer(self, human):
        human.company = self
        self.staff.add(human)

    def make_money(self):
        self.__bank_account.make_money(self.__profit - self.__salary)
        return self.__salary

    def __str__(self):
        return f"{self.name}"
