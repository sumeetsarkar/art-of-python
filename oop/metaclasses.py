"""
Demonstrates few fundamentals of meta classes

Excellent read:
https://realpython.com/python-metaclasses/
"""

# type('', (), {})
# param 1: object or name
# param 2: Base classes
# param 3: Attribute dictionary
# Returns: new type

# Dynamic class Foo created with no bases and no attributes
Foo = type('Foo', (), {})

f = Foo()


def add(self):
    return self.x + self.y

# Dynamic class Bar inheriting class Foo with x, y class variables and instance method add
Bar = type('Bar', (Foo,), {'x':10, 'y':20, 'add':add})

b = Bar()
print(b.add())


# Above class Bar is equivalent to below class Baz
class Baz:
    x = 10
    y = 20

    def add(self):
        return self.x + self.y

b = Baz()
print(b.add())



# Meta classes
class MyMetaClass(type):
    def __new__(cls, name, bases, dct):
        print('Creating Instance MyMetaClass')
        instance = super().__new__(cls, name, bases, dct)
        instance.somecommon_attr = 100
        return instance


class MyClassImpl(metaclass=MyMetaClass):
    def __init__(self):
        print('Creating Instance MyClassImpl')
        pass


m = MyClassImpl()
print(m.somecommon_attr)
