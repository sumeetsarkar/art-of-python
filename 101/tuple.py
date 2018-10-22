"""
Demonstrates handling of return values
"""

import sys

# tuple assingment
justTuple = 1, 2, 3, 4
print(justTuple)

# tuple spread
justTuple1, justTuple2, justTuple3, justTuple4 = 1, 2, 3, 4
print(justTuple1, justTuple2, justTuple3, justTuple4)

# tuple iteration
for n in justTuple:
    print(n)


def get_extremes(arr):
    minVal, maxVal = sys.maxsize, sys.maxsize * -1
    for n in arr:
        if n < minVal:
            minVal = n
        elif n > maxVal:
            maxVal = n
    # returned as tuple
    return minVal, maxVal


# tuple unpacked to individual variables
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
