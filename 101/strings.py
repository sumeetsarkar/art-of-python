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

# Raw strings
print('\n\nRaw strings...')
print(r'\n\nHello')   # prints \n\nhello (no preceeding line breaks)

# String formatting %s
person = {
    'fname': 'Sumeet',
    'lname': 'Sarkar',
    'age': 28,
    'city': 'Bangalore'
}
print('\n\nFormatting using %s ...')
output = 'hello %s' % person['fname']
print(output)

output = '%s is %d years old' % (person['fname'], person['age'])
print(output)

# TypeError, Not enough arguments
# output = '%s is %d years old %s' % (person['fname'], person['age'])

# String formatting .format
print('\n\nFormatting using .format ...')
output = 'hello {}'.format(person['fname'])
print(output)

output = '{1} is {0} years old'.format(person['age'], person['fname'])
print(output)

# IndexError: tuple index out of range
# output = '{1} is {0} years old {2}'.format(person['age'], person['fname'])

# String formatting f strings
print('\n\nFormatting using f strings ...')
output = f"hello {person['fname']}"
print(output)

output = f"{person['fname']} is {person['age']} years old"
print(output)

print(f"{1 == 1}")  # True

# Multiline
output = f"\n{person['fname']} is {person['age']} years old." \
        f" He stays is {person['city']}"

print(output)

# Making {} part of string output
print(f"{{10}} {{{20}}}") # {10} {20} - two or three {} both will print 1 extra pair of braces

print(f"{{{{10}}}}")    # {{10}}  more than three will print extra braces
