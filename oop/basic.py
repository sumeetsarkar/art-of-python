"""
Demonstrates OOP in python
Basic class definition/ attributes and instance attributes/ methods
"""


class Person:
    # class attribute
    someData = 10

    # instance attributes
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # instance methods
    def greet(self):
        return 'Hi, {0} {1}'.format(self.fname, self.lname)


# creating person object
person1 = Person('Sumeet', 'Sarkar')
# executing instance methods
print(person1.greet())

# creating another person object
person2 = Person('John', 'Doe')
print(person2.greet())

# accessing instance attributes directly
print(person1.fname)

# accessing class attribute
print('Person.someData: ', Person.someData)

# accessing class attribute by object
print('person1.someData: ', person1.someData)
# modifying class attribute using object changes the data
person1.someData = 20
print('person1.someData: ', person1.someData)
print('person2.someData: ', person2.someData)

# but accessing the class attribute using Class still shows original value
print('Person.someData: ', Person.someData)

Person.someData = 30
print('Person.someData: ', Person.someData)
# accessing instance variables using Class will cause error
# print(Person.fname) AttributeError: class Person has no attribute 'fname'
