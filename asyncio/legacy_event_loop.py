"""
Demonstrates asyncio without async and await keywords
https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/
"""

import asyncio


def foo():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'


@asyncio.coroutine
def task(name):
    print('{} sleeps for 1 sec'.format(name))
    yield from asyncio.sleep(1)
    print('{} yields for foo'.format(name))
    for c in foo():
        print('{} {}'.format(name, c))


def main():
    tasks = [
        asyncio.ensure_future(task('task A')),
        asyncio.ensure_future(task('task B')),
        asyncio.ensure_future(task('task C')),
    ]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))


main()

print('Executed after main')
