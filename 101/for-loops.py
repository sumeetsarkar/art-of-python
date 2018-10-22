"""
Demostrates different types of for loops
"""

list = ['A', 'B', 'C', 'D', 'E']

# for in loop
print('\nfor in loop:')
for c in list:
    print(c)

# classical range based for loop
print('\nrange(n):')
for i in range(5):
    # range with single param n: starts from 0 to n-1, incrementing 1
    print(i)

print('\nrange(m,n):')
for i in range(3, 5):
    # range with param m,n: starts from m to n-1, incrementing 1
    print(i)

print('\nrange(m,n,o):')
for i in range(3, 5, 2):
    # range with param m,n,o: starts from m to n-1, incrementing o
    print(i)
