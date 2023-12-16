class BankAccount:
    created_account = set()

    def __init__(self, number):
        self.bank_account = f"{number} - bank account"
        if self.bank_account in self.created_account:
            raise ValueError("This bank account already exist")

        self.__amount = 0

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return f"{self.amount}"

    def make_money(self, amount):
        self.__amount += amount
