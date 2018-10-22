"""
Demonstrates class inheritance and polymorphism
"""

# Base class Animal


class Animal:
    def eat(self):
        pass

    def sleep(self):
        print('Animal sleeps')

# class Dog extends Animal


class Dog(Animal):
    def eat(self):
        print('Dog eats')

    def bark(self):
        print('Dog barks')


# Animal object
animal = Animal()
animal.eat()
animal.sleep()

# Dog object, which inherites Animal
dog = Dog()
# Dog eat called as Dog has implemented (specialized) eat instance method of Animal in Dog
dog.eat()
# Animal sleep called as Dog has no special implementation, hence looks up to parent Animal for the method
dog.sleep()
# exculsive instance method bark defined in Dog
dog.bark()


# class Cat extends Animal
class Cat(Animal):
    def eat(self):
        print('Cat eats')

    def purr(self):
        print('Cat purrs')


# class CatHybrid extends Cat and Dog (Order matters)
class CatHybrid(Cat, Dog):
    pass


catHybrid = CatHybrid()
catHybrid.sleep()
# eat instance method of Cat is invoked
catHybrid.eat()

# class DogHybrid extends Dog and Cat (Order matters)


class DogHybrid(Dog, Cat):
    pass


dogHybrid = DogHybrid()
# eat instance method of Dog is invoked
dogHybrid.eat()
