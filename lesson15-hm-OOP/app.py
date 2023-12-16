from OOP_Person import Person
from Factory import Factory
from random import randint


def app():
    john = Person("John", "126u3902945")
    print(john)
    alex = Person("Alex", "29543i5h23958")
    company = Factory("Zaia", 20, randint(5, 8), "94358290it394")
    company.make_offer(john)
    john.work()
    print(john)


app()
