"""
Demonstrating various class instance methods to override
"""


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
        super().__init_subclass__()

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
        super().__new__(cls, *args, **kwargs)
        # Not returning the instance or not calling super will not instantiate the object
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
