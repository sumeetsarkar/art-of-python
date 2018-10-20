from openlib.helper import *

# due to a wildcard import *
# both class Helper and function some_aux_helper_func
# is made available in import_all.py

# create object of Helper
helper = Helper()
helper.help_with_task()

# call func some_aux_helper_func
some_aux_helper_func()
