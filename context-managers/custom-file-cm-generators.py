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


def readFile(filePath, mode):
  f = None
  try:
    f = open(filePath, mode)
    yield f
  except:
    print('File does not exist')
  finally:
    if f is not None:
      f.close()


DIR_NAME = 'data'
FILE_NAME = 'sample2.txt'
FILE_PATH = os.path.join(os.path.dirname(__file__), DIR_NAME, FILE_NAME)

fileGenerator = readFile(FILE_PATH, 'r')

with ContextManager(fileGenerator) as f:
  if f is not None:
    for l in f.readlines():
      print(l)
