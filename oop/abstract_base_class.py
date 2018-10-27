"""
Demonstrates python abstract base classes (ABC)
"""

from abc import ABC, abstractmethod


class Animal():
    @abstractmethod
    def eat(self):
        print('Animal eats')


# since Animal is not inheriting from ABC,
# Animal can be instantiated and abstract method eat is also called
animal = Animal()
animal.eat()


class Dog(Animal):
    pass


# Dog object is created without error
dog = Dog()
dog.eat()


class JustAbstract(ABC):
    def some_method(self):
        print('JustAbstract some method')


# even though JustAbstract inherits ABC, there is no @abstractmethod
# hence, JustAbstract can be instantiated
justAbstract = JustAbstract()
justAbstract.some_method()


class Vehicle(ABC):
    @abstractmethod
    def drives(self):
        pass

    @abstractmethod
    def brakes(self):
        print('Vehicle Brakes')

# vehicle = Vehicle() # TypeError: Can't instantiate abstract class Vehicle with abstract methods drive


class Car(Vehicle):
    pass

# car = Car() # TypeError: Can't instantiate abstract class Car with abstract methods drive


class Ferrari(Car):
    def drives(self):
        print('Ferrari Drives')

    def brakes(self):
        super().brakes()


ferrari = Ferrari()
ferrari.drives()
ferrari.brakes()
