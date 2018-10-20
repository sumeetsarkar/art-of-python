"""
Sample library code
"""

from .helper import some_aux_helper_func, Helper
from .core import Logic, Logging

class Library:
  def __init__(self):
    self.__helper = Helper()
    self.__logger = Logging()
  
  def do_task(self):
    self.__helper.help_with_task()
    some_aux_helper_func()
    Logic().compute()
    self.__logger.log('task completed')
