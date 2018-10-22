from .fileio import FileIO


class Logic:
  
    def compute(self):
        fileio = FileIO()
        fileio.read()
        print('compute')
