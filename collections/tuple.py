""" Demonstrates tuples in python
        packing
        unpacking
        Methods:
            count
            index
"""

import sys

# Tuple assingment
justTuple = 1, 2, 3, 4, 4, 5, 6
print(justTuple)

# Tuple count function returns the number of occurences of given item
print('Tuple count of 2:', justTuple.count(2))
print('Tuple count of 4:', justTuple.count(4))
print('Tuple count of 0:', justTuple.count(0))

# index() Returns the first index of occurence of given item
print('Index of 2:', justTuple.index(2))
print('Index of 4:', justTuple.index(4))
# print('Index of 0:', justTuple.index(0))    # raises ValueError: 0 not in tuple

# Tuple unpack
tu1, tu2, tu3, tu4 = 1, 2, 3, 4
print(tu1, tu2, tu3, tu4)


# Tuple iteration
for n in justTuple:
    print(n)


# A practical example using tuples to return multiple values
def get_extremes(arr):
    minVal, maxVal = sys.maxsize, sys.maxsize * -1
    for n in arr:
        if n < minVal:
            minVal = n
        elif n > maxVal:
            maxVal = n
    # returned as tuple
    return minVal, maxVal


# Tuple unpacked to individual variables
# note: number of explicit members mentioned to unpack variables can be:
# 1 -> recieves tuple
# n, where n equal to tuple length
# m, where m < tuple length: ValueError: too many values to unpack (expected n)
# m, where m > tuple length: ValueError: not enough values to unpack (expected m, got n)
minVal, maxVal = get_extremes([6, 4, 2, 1, 9, 8, 3])
print('min', minVal)
print('max', maxVal)

values = get_extremes([6, 4, 2, 1, 9, 8, 3])
print('tuple', values)
print('min', values[0])
print('max', values[1])
