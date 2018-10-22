"""
Demonstrates a memoisation use case using decorators
"""

# fibonacci series
# 0 1 1 2 3 5 8 13 ...

# fibonacci recursive implementation without memoization


def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print('fibonacci', fibonacci(10))

# fibonacci recursive implementation with memoization


def fibonacciWithMemo(n, mem):
    if n in (0, 1):
        return n
    if n not in mem:
        mem[n] = fibonacciWithMemo(n - 1, mem) + fibonacciWithMemo(n - 2, mem)
    return mem.get(n)


print('fibonacciWithMemo', fibonacciWithMemo(10, {}))

# function based decorator
# we can create a memoize decorator, which memoizes intermediate calculations of recursions in dict


def memoize(fn):
    mem = {}

    def wrapper(*args):
        if args not in mem:
            mem[args] = fn(*args)
        return mem.get(args)
    return wrapper

# using the memoize decorator over a regular recursive fibonacci implementation
# memoize decorator applies the dict based memoization


@memoize
def fibonacciWithDecorator(n):
    if n in (0, 1):
        return n
    return fibonacciWithDecorator(n - 1) + fibonacciWithDecorator(n - 2)


print('fibonacciWithDecorator', fibonacciWithDecorator(10))


# class based decorator
class Memoize:
    def __init__(self, fn):
        self.__mem = {}
        self.__fn = fn

    def __call__(self, *args):
        if args not in self.__mem:
            self.__mem[args] = self.__fn(*args)
        return self.__mem[args]

# using the class based Memoize decorator over a regular recursive fibonacci implementation


@memoize
def fibonacciWithDecoratorClass(n):
    if n in (0, 1):
        return n
    return fibonacciWithDecoratorClass(n - 1) + fibonacciWithDecoratorClass(n - 2)


print('fibonacciWithDecoratorClass', fibonacciWithDecoratorClass(10))


# however, on another note
# for fibonacci one should use Dynamic Programming!
# even better than memoization :)
# above recursive implementation was only for illustration purposes!
def fibonacciDP(n):
    if n <= 0:
        return 0
    list = [1, 1]
    if n in (0, 1):
        return list[n]
    i = 2
    while i != n:
        list.append(list[i - 1] + list[i - 2])
        i += 1
    return list[n - 1]


print('fibonacciDP', fibonacciDP(10))
