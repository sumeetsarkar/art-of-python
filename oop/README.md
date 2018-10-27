# Class

```python

class MyClass:
    def __new__(cls, *args, **kwargs):
        """ called upon object creation """
        print('__new__')
        cls.my_class_variable = 900000  # Defines class variable, not instance variable!
        instance = super().__new__(cls)
        return instance

    def __init__(self, a, b):
        """ object initialization """
        print('__init__')
        self.a, self.b = a, b   # Defines instance variable

    def __init_subclass__(self):
        """ called when a child is subclassed """
        print('__init_subclass__')

    def __call__(self):
        """ on call of object """
        print('__call__')
        return (self.a, self.b)

    def __eq__(self, o):
        """ define equality behaviour """
        print('__eq__')
        if isinstance(o, MyClass):
            return o.a == self.a and o.b == self.b
        raise TypeError('Not MyClass type')

    def __gt__(self, o):
        """ define greater than behaviour """
        print('__gt__')
        if isinstance(o, MyClass):
            return o.a + o.b < self.a + self.b
        raise TypeError('Not MyClass type')

    def __lt__(self, o):
        """ define less than behaviour """
        print('__lt__')
        if isinstance(o, MyClass):
            return o.a + o.b > self.a + self.b
        raise TypeError('Not MyClass type')

    def __add__(self, o):
        """ define addition behaviour """
        print('__add__')
        if isinstance(o, MyClass):
            self.a += o.a
            self.b += o.b
            return self
        raise TypeError('Not MyClass type')
    
    def __sub__(self, o):
        """ define addition behaviour """
        print('__sub__')
        if isinstance(o, MyClass):
            self.a -= o.a
            self.b -= o.b
            return self
        raise TypeError('Not MyClass type')

    def __str__(self):
        """ string upon printing object """
        print('__str__')
        return 'a:{} b:{}'.format(self.a, self.b)
    
    def __repr__(self):
        """ string upon repl output """
        print('__repr__')
        return 'MyClass_instance_a_b'


m1 = MyClass(10, 20)
m2 = MyClass(10, 20)
m3 = MyClass(10, 30)

# Output

# __new__
# __init__
# __new__
# __init__
# __new__
# __init__

print(MyClass.my_class_variable)
# Output

# 900000

print('\n\n---------------------------------------\n\n')

print(m1)
# Output

# __str__
# (10, 20)


print(m1 == m2)
# Output

# __eq__
# True

print(m1())
# Output

# __call__
# True

print(m1 < m3)
# Output

# __lt__
# True

print(m1 > m3)
# Output

# __gt__
# True

print(m1 + m2)
# Output

# __add__
# True

print(m1 - m2)
# Output

# __sub__
# True

print('\n\n---------------------------------------\n\n')

class Child(MyClass):
    def __new__(cls, *args, **kwargs):
        print('__new__Child')
        cls.my_childclass_variable = 100000
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __init__(self, a, b):
        print('__init__Child')
        super().__init__(a, b)

# Subclassing MyClass calls __init_subclass__ in MyClass
# Output

# __init_subclass__

print('\n\n---------------------------------------\n\n')

c1 = Child(1, 2)
# Output

# __new__Child
# __new__
# __init__Child
# __init__

c2 = Child(1, 2)

# Output

# __new__Child
# __new__
# __init__Child
# __init__


print(Child.my_childclass_variable)
# Output

# 100000

print(c1 + c2)
# Output

# a:2 b:4

print('\n\n---------------------------------------\n\n')


class SecondChild(MyClass):
    def __new__(cls, *args, **kwargs):
        return 'Broke the chain of __new__'

    def __init__(self, a, b):
        print('__init__Child')
        super().__init__(a, b)


# Subclassing MyClass calls __init_subclass__ in MyClass
# Output

# __init_subclass__


# Output

sc1 = SecondChild(1, 2)
print(sc1)

# Broke the chain of __new__

```


# Singleton class

If ```__new__``` returns instance of  it’s own class,
then the ```__init__``` method of newly created instance will be invoked with instance
as first(like ```__init__(self, [, ….]```) argument following by arguments passed to ```__new__``` or call of class.
So, ```__init__``` will called implicitly.

If ```__new__``` method return something else other than instance of class, 
then instances ```__init__``` method will not be invoked.
In this case you have to call ```__init__``` method yourself.
```python

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

```


# Metaclasses

```python

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

```