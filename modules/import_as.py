from openlib.helper import Helper as LibHelper

# imports class Helper from module helper.py in openlib as LibHelper
# using 'as' while importing, helps prevent collisions with declarations in current namespace
# as here, class Helper is already declared in this file


class Helper:
    def help_local(self):
        libHelper = LibHelper()
        libHelper.help_with_task()


helper = Helper()
helper.help_local()
