from Bank_account import BankAccount


class Person:
    created_passport = set()

    def __init__(self, person_name, passport_number):
        if passport_number in self.created_passport:
            raise ValueError("This password already exist")

        self.name = person_name
        self.passport = passport_number
        self.__bank_account = BankAccount(self.passport)
        self.company = None

    def work(self):
        if not self.company:
            print("go find you job!")
            return

        salary = self.company.make_money()
        self.__bank_account.make_money(salary)

    def __str__(self):
        return f" Name -{self.name}, Password - {self.passport}, amount - {self.__bank_account}"

