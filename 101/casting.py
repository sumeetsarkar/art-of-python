"""
Demonstrates casting of data types
"""

# casting with int
a = int(10)
b = int('10')
# c = int('10.10') # error, invalid literal for int() with base 10: '1.0', use float
d = int(10.10)

print('\ncasting with int()')
print(a, b, d)


# casting with float
a = float(10)
b = float('10')
c = float('10.10')
d = float(10.10)

print('\ncasting with float()')
print(a, b, c, d)


# casting with str
a = str(10)
b = str(10.10)
c = str("10.10")
d = str(True)
e = str([1, 2, 3])
f = str({'1': 'green', '2': 'blue', '3': 'green'})

print('\ncasting with str()')
print(a, b, c, d, e, f)


# Returns the boolean value of the specified object
print('\ncasting with bool()')
print('bool', bool(False))  # False
print('bool', bool(0))      # False
print('bool', bool(None))   # False
print('bool', bool(True))   # True
print('bool', bool(1))      # True
print('bool', bool('0'))    # True
