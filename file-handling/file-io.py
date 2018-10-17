import os

def create_file_if_not_exists(filename):
  try:
    fileW = open(filename, 'a')
    fileW.write('\nThe quick brown fox jumped over the lazy dog')
  except Exception as e:
    fileW = None
    print(e)
  finally:
    if fileW is not None:
      fileW.close()

def read_file(filename):
  fileR = None
  try:
    fileR = open(filename, 'rt') # (rt) read in text mode is default
    for line in fileR:
      print(line)
  except Exception as e:
    fileR = None
    print(e)
  finally:
    if fileR is not None:
      fileR.close()

DIR = './data'
FILE_NAME = 'sample.txt'
FILE_PATH = os.path.join(os.path.dirname(__file__), DIR, FILE_NAME)

create_file_if_not_exists(FILE_PATH)
read_file(FILE_PATH)
