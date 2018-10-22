"""
Demonstrates a sample implementation of File Context Manager using Generators
"""

import os


class ContextManager:

    def __init__(self, gen):
        self.__gen = gen

    def __call__(self, *args, **kwargs):
        self.__gen = self.__gen(*args, **kwargs)
        return self

    def __enter__(self):
        return next(self.__gen, None)

    def __exit__(self, *args):
        next(self.__gen, None)


def get_file(dir, filename):
    """Returns current dir name prefixed file path
    """
    return os.path.join(os.path.dirname(__file__), dir, filename)


def file_helper(filePath, mode):
    """Generator function taking in file path and io mode
    Yields upon file open and finally closes later
    """
    f = None
    try:
        f = open(filePath, mode)
        yield f
    except Exception as e:
        print('File does not exist', e)
    finally:
        if f is not None:
            f.close()


# Usage of class ContextManager as a decorator
@ContextManager
def file_helper2(filePath, mode):
    """Generator function taking in file path and io mode
    Yields upon file open and finally closes later
    """
    f = None
    try:
        f = open(filePath, mode)
        yield f
    except Exception as e:
        print('File does not exist', e)
    finally:
        if f is not None:
            f.close()


def main():
    print('\nReading file 1...')
    filePath1 = get_file('data', 'sample.txt')
    fileGenerator1 = file_helper(filePath1, 'r')
    # context manager wraps the generator function
    with ContextManager(fileGenerator1) as f:
        if f is not None:
            print(f.read())

    print('\nReading file 2...')
    filePath2 = get_file('data', 'sample2.txt')
    fileGenerator2 = file_helper(filePath2, 'r')
    # context manager wraps the generator function
    with ContextManager(fileGenerator2) as f:
        if f is not None:
            print(f.read())

    # here since ContextManager is already used as a decorator to file_helper2
    # file_helper2 which is essentially a gererator, here acts as a ContextManager
    print('\nReading file 1...')
    with file_helper2(filePath1, 'r') as f:
        if f is not None:
            print(f.read())


if __name__ == '__main__':
    main()
