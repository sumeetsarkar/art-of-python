"""
Demonstrates a sample implementation of File Context Manager using Generators
"""

import os

class ContextManager:
  def __init__(self, gen):
    self.__gen = gen
  
  def __enter__(self):
    return next(self.__gen, None)
  
  def __exit__(self, *args):
    next(self.__gen, None)


def get_file(dir, filename):
  return os.path.join(os.path.dirname(__file__), dir, filename)


def file_helper(filePath, mode):
  f = None
  try:
    f = open(filePath, mode)
    yield f
  except:
    print('File does not exist')
  finally:
    if f is not None:
      f.close()


def read_file(gen):
  with ContextManager(gen) as f:
    if f is not None:
      for l in f.readlines():
        print(l)


print('\nReading file 1...')
filePath1 = get_file('data', 'sample.txt')
fileGenerator1 = file_helper(filePath1, 'r')
read_file(fileGenerator1)

print('\nReading file 2...')
filePath2 = get_file('data', 'sample2.txt')
fileGenerator2 = file_helper(filePath2, 'r')
read_file(fileGenerator2)
