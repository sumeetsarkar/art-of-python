"""
Demonstrates asyncio create task
https://docs.python.org/3/library/asyncio-task.html
"""

import asyncio


async def task(name):
    print('{} sleep for 1 sec'.format(name))
    # sleep() always suspends the current task, allowing other tasks to run.
    await asyncio.sleep(1)
    print('{} sleep for 1 sec again'.format(name))
    await asyncio.sleep(2)
    return '{} completed!'.format(name)


async def main():
    # The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks
    # In Python 3.7+
    taskA = asyncio.create_task(task('task A'))
    taskB = asyncio.create_task(task('task B'))

    # This works in all Python versions but is less readable
    taskC = asyncio.ensure_future(task('task C'))

    # await tasks taskA and taskB, interleaves operations in both the tasks
    await taskA
    await taskB
    await taskC

    print('All tasks completed')


asyncio.run(main())

print('Executed after main')
