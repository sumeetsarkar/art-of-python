"""
Demonstrates encapsulation in classes by private attributes
"""


class Person:
    def __init__(self, fname, lname, age):
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def greet(self):
        return 'Hi, I am {0} {1} and I am {2} years old'.format(self.__fname, self.__lname, self.__age)


person1 = Person('Sumeet', 'Sarkar', 28)
print(person1.greet())

# person1.__age += 1 # error, AttributeError: Person instance has no attribute '__age'

person1.set_age(person1.get_age() + 1)
print(person1.greet())
