"""
Demonstrates an infinite odd/ even number generator
"""


class GenNumbers:
    def __init__(self, base, inc, limit=None):
        self.__base = base
        self.__inc = inc
        self.__limit = limit

    def __iter__(self):
        self.__n = self.__base
        return self

    def __next__(self):
        if self.__limit is not None:
            if self.__n == self.__limit or self.__n + self.__inc > self.__limit:
                raise StopIteration
        self.__n += self.__inc
        return self.__n


# generates even numbers inifnitely, as not limit is passed
numbers = iter(GenNumbers(-2, 2))
print('Even numbers...')
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# generates odd numbers inifnitely, as not limit is passed
numbers = iter(GenNumbers(-1, 2))
print('Odd numbers...')
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# generates odd numbers till limit 10, as not limit is passed
numbers = iter(GenNumbers(-1, 2, 10))
print('Odd numbers...')
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))  # StopIteration
