"""
Handling errors using try except finally
"""

colorCode = -1

try:
    # try some code
    colors = dict(blue=0,
                  green=1,
                  red=2)
    colorCode = colors['red1']
except Exception as e:
    # handle exception
    print('error accessing dictionary, key does not exist:', e)
else:
    print('colorCode', colorCode)
finally:
    # run code which needs to excute regardless of error or not
    print('grace full shutdown')
