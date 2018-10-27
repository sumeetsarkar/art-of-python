"""
Demonstrates following attr methods on classes
    getattr
    hasattr
    delattr
"""


class Point:
    C = 10000
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z


point = Point(10, 20, 30)

# Instance variables
print('hasattr(point, \'x\')', hasattr(point, 'x'))
print('getattr(point, \'x\')', getattr(point, 'x'))
print('delattr(point, \'x\')', delattr(point, 'x'))
print('delattr(point, \'x\')', getattr(point, 'x', None))

# Class Variables
print('hasattr(point, \'C\')', hasattr(Point, 'C'))
print('getattr(point, \'C\')', getattr(Point, 'C'))

# For class variables, delattr cannot operate on instances
# print('delattr(point, \'C\')', delattr(point, 'C'))

# For class variables, instead execute delattr on Class
print('delattr(point, \'C\')', delattr(Point, 'C'))

# print('delattr(point, \'C\')', delattr(Point, 'C'))   # AttributeError, already deleted

print('getattr(point, \'C\')', getattr(Point, 'C', None))

