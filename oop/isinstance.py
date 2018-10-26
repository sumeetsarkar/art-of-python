"""
Demonstrating usage of isinstance
"""


class Animal:
    def eat(self):
        pass


class Dog(Animal):
    def eat(self):
        pass


class Husky(Dog):
    def eat(self):
        pass


animal = Animal()
dog = Dog()
husky = Husky()


print('Husky isinstance of ...')
print(isinstance(husky, Husky))
print(isinstance(husky, Dog))
print(isinstance(husky, Animal))
print(isinstance(husky, (Animal, Dog)))

print('\nDog isinstance of ...')
print(isinstance(dog, Animal))
print(isinstance(dog, Husky))
print(isinstance(dog, (Husky, Animal)))

print('\nHusky subclass of ...')
print(issubclass(Husky, Dog))
print(issubclass(Dog, Husky))
