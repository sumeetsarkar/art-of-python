def foo():
    yield 'a'
    yield 'b'
    yield 'c'


def bar():
    yield foo()
    yield 'd'
    yield 'e'
    yield 'f'


def baz():
    yield from foo()
    yield 'd'
    yield 'e'
    yield 'f'


print('yield foo()')
for c in bar():
    print(c)

print('yield from foo()')
for c in baz():
    print(c)
