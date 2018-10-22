"""
Demonstrates the usage of class doc string __doc__
"""


class Person:
    """ Defines a Person class
    attributes:
      fname (str):
      lname (str):
      age (int):
    """

    def __init__(self, fname, lname, age):
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    def greet(self):
        return 'Hi, I am {0} {1} and I am {2} years old'.format(self.__fname, self.__lname, self.__age)


person = Person('Sumeet', 'Sarkar', 28)
print(Person.__doc__)
print(person.__doc__)

person.__doc__ = 'Hello'
print(Person.__doc__)
print(person.__doc__)

Person.__doc__ = 'Hello'
print(Person.__doc__)
print(person.__doc__)

print(__doc__)
