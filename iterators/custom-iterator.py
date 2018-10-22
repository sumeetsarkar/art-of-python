"""
Demonstrates building a custom iterator
"""


class GenNumers:
    def __init__(self, limit):
        self.__limit = limit

    def __iter__(self):
        self.__n = 0
        # important! has to return self
        return self

    def __next__(self):
        if (self.__limit == self.__n):
            raise StopIteration
        self.__n += 1
        return self.__n


numbers = GenNumers(10)
# for loop iteration, internally for loop applies iter(numbers) and loops on the next()
for i in numbers:
    print(i)

# or, apply iter() on iterable object -> implements __iter__ & __next__
# below code deconstructs for i in iterator: loop
numbers = iter(GenNumers(10))
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break
