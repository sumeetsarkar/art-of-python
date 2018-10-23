"""
Demonstrates use cases of generators
"""

import time


def compute():
    for x in range(5):
        time.sleep(.5)
        yield x


# directly calling a function implementing yield inside will return generator object
genObject = compute()
print(genObject)  # prints generator object

# generator individual iterate
print('\nIterate as next(genObject)')
while True:
    try:
        print(next(genObject))
    except StopIteration:
        break


# generator methods can be iterated over
print('\nIterate using for in loop')
for n in compute():
    print(n)

# get iterator of generator and iterate over
print('\nIterate using iter(genObject)')
iterator = iter(compute())
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
