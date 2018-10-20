from openlib import helper
from openlib.library import Library

# both are valid forms of import

# 1st, from openlib import helper
# we mention importing helper module from openlib
# hence, we get access to both class Helper and func some_aux_helper_func in helper

helper.Helper().help_with_task()
helper.some_aux_helper_func()


# 2nd, from openlib.library import Library
# we mention to import specific class Library from module library inside package openlib
# hence, only the class Library is added to current namespace and not the func some_other_lib_func from library module

Library().do_task()

# some_other_lib_func() # error, NameError: name 'some_other_lib_func' is not define
