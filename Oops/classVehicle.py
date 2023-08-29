from abc import ABC,abstractmethod
class vechicle(ABC):
    @abstractmethod
    def ride(self):
        pass
class car(vechicle):
    def ride(self):
        if (__name__ == '__main__'):
            print("You are working on main class")
            print(__name__)
        print("Your Riding Car")
class bike(vechicle):
    def ride(self):
        print("Your Riding Bike")
car1=car()
car1.ride()