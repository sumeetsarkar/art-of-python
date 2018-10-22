"""
Demonstrates basic use case of decorators
"""

import time


def add(a, b):
    return a + b


def compute_time(fn):
    """Returns a wrapper function which can take arguments
    and call decorated function with the arguments and add additional functionality to it
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(fn.__name__, 'time elapsed: ', end - start)
    return wrapper


add = compute_time(add)
add(1, 2)

# or


@compute_time
def add_with_decorator(a, b):
    return a + b


add_with_decorator(1, 2)
