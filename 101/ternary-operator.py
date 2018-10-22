"""
Demonstrates 3 different ways to implement ternary operations
"""


a, b = 10, 20

# explicit if else
min = a if a < b else b
print(min)

# tuple index, true -> 1, false -> 0
min = (b, a)[a < b]
print(min)

# dict, True, False keys
min = {True: a, False: b}[a < b]
print(min)
