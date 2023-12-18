from cars import Car
from house import House
from person import Person


def app():
    john = Person("John")
    while john.bank_account.balance < 140:
        john.work()
    print(john)
    car = Car()
    john.buy_car(car)
    print(john)
    house = House()
    john.buy_house(house)
    print(john)
    john.sell_house(house)
    print(john)
    john.sell_car(car)
    print(john)


app()
