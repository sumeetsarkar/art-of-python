import os

def create_file_if_not_exists(filename):
  fileW = open(filename, 'a')
  fileW.write('\nThe quick brown fox jumped over the lazy dog')

def read_file(filename):
  try:
    fileR = open(filename, 'rt') # (rt) read in text mode is default
    for line in fileR:
      print(line)
  except:
    print('File does not exsits')

DIR = './data'
FILE_NAME = 'sample.txt'
FILE_PATH = os.path.join(DIR, FILE_NAME)

create_file_if_not_exists(FILE_PATH)
read_file(FILE_PATH)
