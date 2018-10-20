import openlib.library
from openlib import helper

lib = openlib.library.Library()
lib.do_task()

# both are valid
helperObj = helper.Helper()  # using import to access class defined in helper.py
helperObj = openlib.helper.Helper()  # explicit usage of fully qualified path, does not require any import

helperObj.help_with_task()
helper.some_aux_helper_func()
