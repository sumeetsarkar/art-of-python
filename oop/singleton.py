"""
Demonstrating implementation of Singleton class in python

If __new__ returns instance of  it’s own class,
then the __init__ method of newly created instance will be invoked with instance
as first(like __init__(self, [, ….]) argument following by arguments passed to __new__ or call of class.
So, __init__ will called implicitly.

If __new__ method return something else other than instance of class, 
then instances __init__ method will not be invoked.
In this case you have to call __init__ method yourself.
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, somedata):
        self.somedata = somedata

    def __str__(self):
        return str(self.somedata)


s1 = Singleton(10)
print(s1)   # 10

s1.somedata += 10
print(s1)   # 20

s2 = Singleton(100)
print(s2)   # 100
print(s1)   # 100

