"""
Collections package default dict
"""

from collections import defaultdict

# defaultdict takes a function without arguments
# to return default values of key is not found (i.e., _getitem_)

# defaultdict compares equals to any other dict with same items

defdict = defaultdict(lambda: 'NA')
defdict['r'] = 'RED'
defdict['g'] = 'GREEN'
defdict['b'] = 'BLUE'

print(defdict['r'])
print(defdict['rgb'])   # Does not cause KeyError, instead prints NA

# Another example
from random import randint

defdict = defaultdict(lambda: randint(0, 10))
print(defdict['K'])     # prints a random number from 0-10 if key not found
