"""
Demonstrating class __str__ function usage
"""


class Student:
    def __init__(self, fname, lname, age):
        self.__fname, self.__lname, self.__age = fname, lname, age

    def __str__(self):
        return 'name: {} {}, age: {}'.format(self.__fname, self.__lname, self.__age)


s = Student('Sumeet', 'Sarkar', 28)
# Prints the string return from implicit call of __str__ function
print(s)
