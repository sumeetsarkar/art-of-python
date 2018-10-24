# Context Managers

Context managers are an efficient way to wrap around enter and exit logic for a piece of code that performs on the resource on which enter and exit logic applies.

It is a clean way of wrapping the code, to make sure no matter the operation being performed on the resource completes or raises an exception, the exit logic will always be executed.

For any class to be a context manager, it should implement ```__enter__``` and ```__exit__``` methods

```python
class MyContextManager:

    def __enter__(self):
        pass
    
    def __exit__(self):
        pass
```

## Invoking a Context Manager

A context manager is invoked using ```with``` keyword. It may or may not return a resource to be worked on. We will see various examples of it further.

A file can be opened as a context manager or a more traditional way. Let us examine both approaches.

```python
# A traditional file write

# Open file
f = open('my_file.txt', 'a')

# Perform write operation on file
f.write('The quick brown fox jumped over the lazy dog')

# Explicitly close the file
f.close()
```

So the pattern we see is that, to operate on the resource, we perform some 'on enter ' operation on it, then perform the operation and finally to mark completion, we perform the 'on exit' operation

This puts a lot of maintenance on the developer and may lead to scenarios, when the 'on exit' operation might never be performed.

```python
# Open file
f = open('my_file.txt', 'a')

# Perform write operation on file
f.write('The quick brown fox jumped over the lazy dog')

# Simulate an exception occured
raise Exception('some exception you knew could occur')

# Explicitly close the file
f.close()
```

In the above scenario, the ```f.close()``` is never executed

To prevent this on might wrap around the code in a ```try except finally``` block, like below.

```python
f = None
try:
    # Open file
    f = open('my_file.txt', 'a')

    # Perform write operation on file
    f.write('The quick brown fox jumped over the lazy dog')

    # Simulate an exception occured
    raise Exception('some exception you knew could occur')
except:
    print('Oops exception!')
finally:
    if f is not None:
        f.close()
```

Here, we see the job get done! But that is too many lines of code and carefully thought of flow of execution to be able to close a resource. Think how this would from more nested and cumbersome to maintain, upon accessing nested resources! Check the example [contextlib_example.py](https://github.com/sumeetsarkar/art-of-python/blob/master/context_managers/contextlib_example.py) to see the clean nesting with context managers


## Using Context Managers

```python
# Open file using open() as Context Manager

with open('my_file.txt', 'a') as f:
    f.write('The quick brown fox jumped over the lazy dog')

# And you are done!
# Context Manager will take care of the exit logic,
# which here is f.close()
```


## Implementing a Context Manager

As discussed above, to write a context manager class, the class must implement the ```__enter__``` and ```__exit__``` methods. So let us implement a File context manager, working on the ```open``` and ```close``` methods of the file. Even though as we just saw in above example file open is already a context manager, but for now lets say we need to implement one!

```python
class FileCM:
    def __init__(self, filePath, mode):
        """Sets the filePath and mode"""
        self.__filePath = filePath
        self.__mode = mode

    def __enter__(self):
        """Opens the file with filepath and mode
        Returns the file instance
        """
        self.__f = open(self.__filePath, self.__mode)
        return self.__f

    def __exit__(self, *args):
        """Closes the file on exit"""
        self.__f.close()


# Access context manager using with keywork
with FileCM('sample.txt', 'r') as f:
    print(f.read())
```


A practical illustration of using context managers in threading Lock

```python
from threading import Lock

class Task:
    def __init__(self):
        self.__lock = Lock()

    def __do_some_uncertain_task_1(self):
        # Acquires lock as a context manager
        with self.__lock:
            raise Exception('some error you knew may happen!')

    def __do_some_uncertain_task_2(self):
        # Acquires lock
        self.__lock.acquire()
        raise Exception('some error you knew may happen!')
        # Code here is unreachable as before lock release the exception is raised
        self.__lock.release()

    def initiate(self):
        try:
            # __do_some_uncertain_task_1 is safe to user here
            self.__do_some_uncertain_task_1()
            # __do_some_uncertain_task_2 will raise exception and not release the lock
            # upon catching the exception the code will be blocked to proceed further as lock cannot be acquired
            self.__do_some_uncertain_task_2()
            # 
        except:
            print('Caught exception')
        self.__lock.acquire()


# Code execution finishes gracefully
Task().initiate()
```


## Fun with context manager using context lib

Here is a small sample below, expressing the idea. A better implementation is at [contextlib_example.py](https://github.com/sumeetsarkar/art-of-python/blob/master/context_managers/contextlib_example.py)

```python
from contextlib import contextmanager

@contextmanager
def tag(tagname):
    print('<{}>'.format(tagname))
    yield
    print('<\{}>'.format(tagname))

with tag('html'):
    with tag('div'):
        with tag('h1'):
            print('Context Managers')
        with tag('p'):
            print('Hello World!')

# Outputs
#
# <html>
# <div>
# <h1>
# Context Managers
# <\h1>
# <p>
# Hello World!
# <\p>
# <\div>
# <\html>
```
