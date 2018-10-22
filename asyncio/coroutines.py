"""
Demonstrates asyncio coroutines
https://docs.python.org/3/library/asyncio-task.html
"""

import asyncio


async def task(name):
    print('{} sleep 1 sec'.format(name))
    # await for sleep for 1 seconds
    await asyncio.sleep(1)
    print('{} sleep 1 sec again'.format(name))
    # await for sleep for 1 seconds
    await asyncio.sleep(1)
    return 100


# @asyncio.coroutine is a Decorator to mark generator-based coroutines
# This decorator enables legacy generator-based coroutines to be compatible with async/await code:
@asyncio.coroutine
def task_older(name):
    print('{} sleep 1 sec'.format(name))
    yield from asyncio.sleep(1)
    return 100


async def main():
    # A coroutine object is created but not awaited, hence task will never run at all
    task('task Dormant')  # RuntimeWarning: coroutine 'task' was never awaited

    # awaiting async task, each of these will be awaited to completion sequentially
    result1 = await task('task A')
    result2 = await task('task B')
    result3 = await task_older('task C')
    print(result1 + result2 + result3)


# No toplevel awaits, await can only ber perfomed inside async functions
# await main()  # error, SyntaxError: 'await' outside function

# asyncio run coroutine
asyncio.run(main())

print('Executed after main')
