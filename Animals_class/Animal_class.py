class Moving:
    def move(self):
        raise NotImplementedError(
            'Define voice in %s.' % self.__class__.__name__)


class Animal(Moving):
    def voice(self):
        raise NotImplementedError(
            'Define voice in %s.' % self.__class__.__name__
        )


class Transport(Moving):
    def launch(self):
        raise NotImplementedError(
            'Define voice in %s.' % self.__class__.__name__
        )


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
    def __init__(self):
        self.status = "non launch"

    def move(self):
        if self.status == "non launch":
            print("Car ain`t moving")
        elif self.status == "launch":
            print("Car is rides")

    def launch(self):
        if self.status == "non launch":
            self.status = "launch"
            print(self.status)


