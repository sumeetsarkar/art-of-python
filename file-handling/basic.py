"""
Demonstrates basic file IO operations in python

Please Note:

This sample code does not leverage ContextManagers
and demonstrates basic usage of open()

File Context Managers are explained well in the context-managers section
"""

import os


def create_file_if_not_exists(filePath):
    """Creates a file if not exists
    parameters:
      filePath: path of file to create/ write on to
    """
    fileW = None
    try:
        # opens file in append mode (creates if not exists)
        fileW = open(filePath, 'a')
        # write to file, below text prefixes with \n, which adds text in new line
        fileW.write('\nThe quick brown fox jumped over the lazy dog')
    except Exception as e:
        print(e)
    finally:
        # if fileW was not None, close the file
        if fileW is not None:
            fileW.close()


def read_file(filePath):
    """Reads a file
    parameters:
      filePath: path of file to read from to
    """
    fileR = None
    try:
        # (rt) read in text mode is default
        fileR = open(filePath, 'rt')
        # iterate of the file lines and print each line
        for l in fileR.readlines():
            print(l)
    except Exception as e:
        print(e)
    finally:
        # if fileR was not None, close the file
        if fileR is not None:
            fileR.close()


def get_fully_qualified_file_path(dir, file):
    return os.path.join(os.path.dirname(__file__), dir, file)


# get fully qualified path
filePath = get_fully_qualified_file_path('./data', 'sample.txt')
# create/ write file
create_file_if_not_exists(filePath)
# read file
read_file(filePath)
