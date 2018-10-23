"""Demonstrates Lock from threading used as Context Manager

Similar to File, Lock should also be used as Context Manager to release lock if there is any exception
"""

from threading import Lock


# Example 1, where in Lock is used without context manager

class Task:
    def __init__(self):
        self.__lock = Lock()

    def __do_some_uncertain_task(self):
        # Acquires lock
        self.__lock.acquire()
        raise Exception('some error you knew may happen!')
        # Code here is unreachable as before lock release the exception is raised
        self.__lock.release()
    
    def initiate(self):
        try:
            self.__do_some_uncertain_task()
        except:
            print('Caught exception')
        # Here the exceptation is to acquire the lock, 
        # but since it is never release, code cannot proceed further
        self.__lock.acquire()


class BetterTask:
    def __init__(self):
        self.__lock = Lock()
    
    def __do_some_uncertain_task(self):
        with self.__lock:
            raise Exception('some error you knew may happen!')
    
    def initiate(self):
        try:
            self.__do_some_uncertain_task()
        except:
            print('Caught exception')
        self.__lock.acquire()


# Code execution finishes gracefully
BetterTask().initiate()

# Code execution hangs, unable to acquire lock
Task().initiate()
