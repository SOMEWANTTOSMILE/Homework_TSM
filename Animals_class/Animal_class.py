class Moving:
    def move(self):
        raise NotImplementedError(
            'Define voice in %s.' % self.__class__.__name__)


class Animal(Moving):
    def voice(self):
        raise NotImplementedError(
            'Define voice in %s.' % self.__class__.__name__)


class Transport(Moving):
    def launch(self):
        raise NotImplementedError(
            'Define voice in %s.' % self.__class__.__name__)


class Duck(Animal):
    def voice(self):
        print("duck quacks")

    def move(self):
        print("Duck is swimming")


class Tiger(Animal):
    def voice(self):
        print("tiger growls")

    def move(self):
        print("Tiger is running")


class Car(Transport):
    def __init__(self, status=None):
        self.status = status

    def move(self):
        if self.status == "non launch":
            print("Car ain`t moving")
        elif self.status == "Launch":
            print("Car is rides")

    def launch(self):
        if self.status is None:
            self.status = 'Launch'
            print("launch")
        elif self.status is not None:
            self.status = 'non launch'
            print("non launch")
