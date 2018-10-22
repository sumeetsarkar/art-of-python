"""
Demonstrates usage of global in python
Understanding local and global variable scopes
"""


def foo():
    print(s)


s = 'Test outside'
foo()
print(s)


print('\n\n-------------------------------')


def bar():
    # UnboundLocalError: local variable 's' referenced before assignment
    # print(s)  # since s is used before declared in local scope
    s = 'Test inside foo'
    print(s)  # Test inside foo


s = 'Test outside'
bar()
print(s)


print('\n\n-------------------------------')


def baz():
    global s
    print(s)
    s = 'Test inside baz'
    print(s)


s = 'Test outside'
baz()
print(s)


print('\n\n-------------------------------')


def bazz():
    s = 'Test inside bazz'

    def inner():
        global s
        s = 'Test inside bazz inner'
    print(s)
    inner()
    print(s)


s = 'Test outside'
bazz()
print(s)
