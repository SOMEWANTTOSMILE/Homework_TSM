from random import randint


class Person:
    def __init__(self, person_name):
        self.name = person_name
        self.bank_account = 0
        self.person_property = False


class Work(Person):
    def work(self):
        salary = randint(5, 8)
        self.bank_account = self.bank_account + salary


class Car(Person):
    def __init__(self, person_name):
        super().__init__(person_name)
        self.car_price = 40


class Property(Person):
    def __init__(self, person_name):
        super().__init__(person_name)
        self.property_price = 100


