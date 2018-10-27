"""
Demonstrating json loads and dump
"""

import json

# Basic
person = {"fname": "Sumeet", "lname": "Sarkar", "age": 28}
strdata = json.dumps(person)
print('string data', strdata)
person = json.loads(strdata)
print('dict data', person)


# Using class
class Student:
    def __init__(self, fname, lname, age):
        self.__fname, self.__lname, self.__age = fname, lname, age

    def __str__(self):
        return 'name: {} {}, age: {}'.format(self.__fname, self.__lname, self.__age)


jsonstring = '{ "fname": "Sumeet", "lname": "Sarkar", "age": 28 }'

obj = json.loads(jsonstring, object_hook=lambda d: Student(d['fname'], d['lname'], d['age']))
print(obj)

print(json.dumps(obj, default=lambda o: o.__dict__))