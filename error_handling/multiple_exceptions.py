"""
Handling multiple exceptions
"""

from random import randint

try:
    num = randint(0, 10)
    if num < 2:
        raise ValueError('Random number less than 2')
    elif num > 5:
        raise IndexError('Random number greater than 5')
    else:
        print(num)
    # Except multiple types of Errors to handle
except (ValueError, IndexError) as e:
    print(e)
