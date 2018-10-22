"""
Demonstrates basic usage of an inbuilt context manager for File
"""

import os

DIR_NAME = 'data'
FILE_NAME = 'sample.txt'
FILE_PATH = os.path.join(os.path.dirname(__file__), DIR_NAME, FILE_NAME)

with open(FILE_PATH) as f:
    for l in f.readlines():
        print(l)
