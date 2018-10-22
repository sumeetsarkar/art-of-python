"""
Demonstrates a iterator in python

Python iterator object must implement two special methods,
__iter__() and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it.

Most of built-in containers in Python like: list, tuple, string etc. are iterables.
"""

list = [1, 2, 3, 4]

# print(next(list)) # error, TypeError: 'list' object is not an iterator
# to be able to use next() to iterate over the list, it needs to be converted to an iterator
# using iter()

listIter = iter(list)
print(listIter)  # list_iterator object

print(next(listIter))  # 1
print(next(listIter))  # 2
print(next(listIter))  # 3
print(next(listIter))  # 4
# print(next(listIter)) # raises StopIteration

# iterator , once exhausted of items will raise StopIteration

# this is exactly how a python for loop iterates over iterables

"""
for element in iterable:
    # do something with element
"""

listIter = iter(list)  # building an iterator over list

while True:
    try:
        print(next(listIter))
    except StopIteration:
        break
