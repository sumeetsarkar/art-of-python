"""
Demonstrating various class instance methods to override
"""


class MyClass:
    def __new__(cls, *args, **kwargs):
        print('__new__')
        instance = object.__new__(cls)
        return instance

    def __init__(self, a, b):
        """ object initialization """
        print('__init__')
        self.a, self.b = a, b

    def __call__(self):
        """ on call of object """
        print('__call__')
        return (self.a, self.b)

    def __eq__(self, o):
        """ define equality behaviour """
        print('__eq__')
        if isinstance(o, MyClass):
            return o.a == self.a and o.b == self.b

    def __gt__(self, o):
        """ define greater than behaviour """
        print('__gt__')
        if isinstance(o, MyClass):
            return o.a + o.b < self.a + self.b

    def __lt__(self, o):
        """ define less than behaviour """
        print('__lt__')
        if isinstance(o, MyClass):
            return o.a + o.b > self.a + self.b

    def __str__(self):
        """ string upon printing object """
        print('__str__')
        return 'a:{} b:{}'.format(self.a, self.b)
    
    def __repr__(self):
        """ string upon repl output """
        print('__repr__')
        return 'MyClass_instance_a_b'


m1 = MyClass(10, 20)
print(m1)

m2 = MyClass(10, 20)
print(m1 == m2)

print(m1())

m3 = MyClass(10, 30)
print(m1 < m3)
print(m1 > m3)
