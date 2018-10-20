import openlib.library
import openlib.core.fileio
import openlib.core

# here the import syntax just mentions import
# which in turn adds the specific module in current namespace
# since, we do not specify any particular class/ func to be imported

# this form of import is actually similar to
# from openlib import library

# But, here we need to use the fully qualified name of the module to access class/ functions in the module

# fully qualified name to access func some_other_lib_func in openlib.library
openlib.library.some_other_lib_func()

# fully qualified name to access class FileIO in openlib.core.fileio
openlib.core.fileio.FileIO().read()

# fully qualified name to access func some_core_function_exposed in __init__.py in core
openlib.core.some_core_function_exposed()
