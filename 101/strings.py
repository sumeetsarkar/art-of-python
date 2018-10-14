"""
Demonstrates string operations in python
"""

# string concatenation
fname = 'Sumeet'
lname = 'Sarkar'
print('Hi ' + fname + ' ' + lname)

# string and other data type variable concatenation
# print(fname + ' is ' + 28 + ' years old') # error, TypeError: cannot concatenate 'str' and 'int' objects
print(fname + ' is ' + str(28) + ' years old')

# string format
greetUser = 'Hi, I am {0} {1} and I am {2} years old'
# int to string casting is not needed when passing argument to format
print(greetUser.format(fname, lname, 28))

# char at index
print('Hello World'[4])

# substring
print('Hello World'[2:4])

# len
print(len('Hello World'))

# upper case
print('Hello World'.upper())

# lower case
print('Hello World'.lower())

# strip
print('   Hello World   '.strip())

# split
tokens = 'Hello:world'.split(':')
print(tokens)
