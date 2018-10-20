"""
Sample library code
"""

from .helper import Helper, some_aux_helper_func
from .core import Logic, Logging, some_core_function_exposed
# from .core import Logic, Logging, FileIO  # FileIO import will not work
# as module core __init__.py is not empty and does not explicitly import FileIO
# adding below import in __init__.py in core module, will allow FileIO to be imported here
# from .fileio import FileIO

class Library:

  def __init__(self):
    self.__helper = Helper()
    self.__logger = Logging()
  
  def do_task(self):
    self.__helper.help_with_task()
    some_aux_helper_func()
    Logic().compute()
    some_core_function_exposed()
    self.__logger.log('task completed')
