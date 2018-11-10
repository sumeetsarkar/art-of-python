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


def add(cls):
    return cls.x + cls.y

# Dynamic class Bar inheriting class Foo with x, y class variables and instance method add
Bar = type('Bar', (Foo,), {'x':10, 'y':20, 'add':add})

b = Bar()
print(b.add())


# Above class Bar is equivalent to below class Baz
class Baz:
    x = 10
    y = 20

    def add(self):
        return Baz.x + Baz.y

b = Baz()
print('Baz add', b.add())



# Meta classes
class MyMetaClass(type):
    def __new__(cls, name, bases, dct):
        print('__new__MyMetaClass')
        instance = super().__new__(cls, name, bases, dct)
        instance.somecommon_attr = 100
        cls.class_varable = 200
        # Read explanation below for DerviedClass
        if name == 'DerviedClass' and 'please_implement' not in dct:
            raise TypeError('Bad user derived class, please_implement should be overried!')
        return instance


class MyClassImpl(metaclass=MyMetaClass):
    def __init__(self):
        print('__init__MyClassImpl')

# Output

# __new__MyMetaClass

m = MyClassImpl()
print(m.somecommon_attr)    # attr instance variable injected by MyMetaClass 
print(MyClassImpl.class_varable)    # attr class variable injected by MyMetaClass 

# Output

# __init__MyClassImpl
# 100
# 200


class MyLibrary(metaclass=MyMetaClass):
    def __init__(self):
        print('__init__MyLibrary')
    
    def please_implement(self):
        pass

# Output

# __new__MyLibrary


class DerviedClass(MyLibrary):
    def __init__(self):
        print('__init__DerviedClass')

# Output

# TypeError: Bad user derived class, please_implement should be overried

# This is one of the most significant use cases of Meta Classes
# Since, DerviedClass inherits MyLibrary, 
# it is expected that the child class should implement a please_implement() instance method
# But how do we enforce it?
# Since MyLibrary has MyMetaClass as the metaclass
# Whenever any child class inhertis MyLibrary, the MyMetaClass __ini__ is called
# Arguments to which are interestingly the type arguments
# type('', (), {})
# param 1: object or name
# param 2: Base classes
# param 3: Attribute dictionary
# Returns: new type
# Hence, we can easily determine,
# the deriving class name and methods in dict and take appropriate actions