"""
Different Types in python
"""

def func():
    pass


class Sample:
    pass


# Types of data
print('string', type(''))
print('0', type(0))
print('1.0', type(1.0))
print('True', type(True))
print('[]', type([]))
print('{}', type({}))
print('{0}', type({0}))
print('()', type(()))
print('lambda', type(lambda a: 10))
print('func', type(func))
print('Class()', type(Sample()))
print(None, type(None))

# Output

# string <class 'str'>
# 0 <class 'int'>
# 1.0 <class 'float'>
# True <class 'bool'>
# [] <class 'list'>
# {} <class 'dict'>
# {0} <class 'set'>
# () <class 'tuple'>
# lambda <class 'function'>
# func <class 'function'>
# Class() <class '__main__.Sample'>
# None <class 'NoneType'>


# Types of types (Meta Data)
print('\n\n-----------------')
print('str', type(str))
print('int', type(int))
print('float', type(float))
print('float', type(bool))
print('list', type(list))
print('dict', type(dict))
print('set', type(set))
print('tuple', type(tuple))
print('type', type(type))
print('class Sample', type(Sample))

# Output

# str <class 'type'>
# int <class 'type'>
# float <class 'type'>
# float <class 'type'>
# list <class 'type'>
# dict <class 'type'>
# set <class 'type'>
# tuple <class 'type'>
# type <class 'type'>
# class Sample <class 'type'>