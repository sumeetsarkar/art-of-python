# Function based decorator
def twice(func):
    def wrapped(*args, **kwargs):
        return func(2, *args, **kwargs)
    return wrapped


# Class based decorator
class Twice:
    def __init__(self, func):
        self.__func = func
        Twice.MULTIPLIER = 2

    def __call__(self, *args, **kwargs):
        return self.__func(Twice.MULTIPLIER, *args, **kwargs)


@twice
def multiply_decorated_by_func(a, b):
    return a*b


@Twice
def multiply_decorated_by_class(a, b):
    return a*b


print(multiply_decorated_by_func(4))

print(multiply_decorated_by_class(4))
