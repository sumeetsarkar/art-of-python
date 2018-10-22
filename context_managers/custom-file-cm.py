"""
Demonstrates a sample implementation of File Context Manager

A python context manager object must implement two special methods,
__enter__() and __exit__()
"""

import os


class FileCM:
    def __init__(self, filePath, mode):
        self.__filePath = filePath
        self.__mode = mode

    def __enter__(self):
        self.__f = open(self.__filePath, self.__mode)
        return self.__f

    def __exit__(self, *args):
        self.__f.close()


DIR_NAME = 'data'
FILE_NAME = 'sample.txt'
FILE_PATH = os.path.join(os.path.dirname(__file__), DIR_NAME, FILE_NAME)

with FileCM(FILE_PATH, 'r') as f:
    for line in f.readlines():
        print(line)
