# Returns the absolute value of a number
num = -1
print('abs', abs(num))  # 1

# Returns True if all items in an iterable object are true
print('all', all(''))   # True
print('all', all('a'))  # True
print('all', all([]))   # True
print('all', all([0]))  # False
print('all', all([0, 1, 1]))    # False
print('all', all([1, 1, 1]))    # True
print('all', all(['0', 1, 1]))  # True

# Returns True if any item in an iterable object is true
print('any', any([]))       # False
print('any', any([0]))      # False
print('any', any([0, 1]))   # True

# all([]) = True, any([]) = False

# Returns a readable version of an object. Replaces none-ascii characters with escape character
print('ascii', ascii('A!#@'))   # A!#@

# Returns binary version of a number
print('bin', bin(13))    # 0b1101

# Returns the boolean value of the specified object
print('bool', bool(False))  # False
print('bool', bool(0))      # False
print('bool', bool(None))   # False
print('bool', bool(True))   # True
print('bool', bool(1))      # True
print('bool', bool('0'))    # True

# Returns an array of bytes
print('bytearray', bytearray('Sumeet', 'UTF8'))
print('bytearray', bytearray(1))
print('bytearray', bytearray([0, 1, 2]))

# Returns a bytes object
print('bytes', bytes(0))
print('bytes', bytes(1))
print('bytes', bytes('S', 'UTF8'))

# Returns True if the specified object is callable, otherwise False
print('callable', callable(print))  # True
print('callable', callable(num))    # False

# Returns a character from the specified Unicode code.
print('chr', chr(65))   # A
print('chr', chr(97))   # a

# Deletes the specified attribute (property or method) from the specified object
class Person:
    name = 'Sumeet'
    city = 'Bangalore'

print('delattr', delattr(Person, 'city'))  # None
# print('delattr', delattr(Person, 'city')) # deleting key not present will cause AttributeError

# Without arguments, return the list of names in the current local scope.
# With an argument, attempt to return a list of valid attributes for that object.
print('dir() local scope', dir())
print('dir(Person)', dir(Person))

# Take two (non complex) numbers as arguments and 
# return a pair of numbers consisting of their quotient and remainder when using integer division
print('divmod(49, 2)', divmod(49, 2))
print('divmod(48, 2)', divmod(48, 2))

# Return the largest item in an iterable or the smallest of two or more arguments.
print('max', max(1,2,3,4))
print('max', max([1,2,3,4]))

# Return the smallest item in an iterable or the smallest of two or more arguments.
print('min', min(1,2,3,4))
print('min', min([1,2,3,4]))

# zip
# Example 1
odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]
# Returns an iterator of tuples, of pairs of ith item from each list until the smallest list
zipped = zip(odd, even)
tuplelist = list(zipped)
print(tuplelist)
# Output
# [(1, 2), (3, 4), (5, 6), (7, 8)]

# Example 2
l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40, 50, 60]
l3 = [100, 200, 300 ]
tuplelist = list(zip(l1, l2, l3))
print(tuplelist)
# Output
# [(1, 10, 100), (2, 20, 200), (3, 30, 300)]

# Example 3
tuplelist = list(zip(l1))
print(tuplelist)
# Output
# [(1,), (2,), (3,), (4,), (5,), (6,)]

# str Prints the string
print('str(1)', str(1))
print('str(1.0)', str(1.0))
print('str(\'1\')', str('1'))
print('str(True)', str(True))

# sum Gets sum of iterable with an option start param
print('sum([1,2,3,4])', sum([1,2,3,4]))
print('sum([1,2,3,4], 10)', sum([1,2,3,4], 10))
