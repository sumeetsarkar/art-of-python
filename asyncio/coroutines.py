"""
Demonstrates asyncio coroutines
https://docs.python.org/3/library/asyncio-task.html
"""

import asyncio


async def task():
  # await for sleep for 1 seconds
  await asyncio.sleep(1)
  # await for sleep for 1 seconds
  await asyncio.sleep(1)
  return 100


# @asyncio.coroutine is a Decorator to mark generator-based coroutines
# This decorator enables legacy generator-based coroutines to be compatible with async/await code:
@asyncio.coroutine
def task_older():
  yield from asyncio.sleep(1)
  return 100


async def main():
  # A coroutine object is created but not awaited, hence task will never run at all
  task()  # RuntimeWarning: coroutine 'task' was never awaited

  # awaiting async task
  result1 = await task()
  result2 = await task_older()
  print(result1 + result2)


# No toplevel awaits, await can only ber perfomed inside async functions
# await main()  # error, SyntaxError: 'await' outside function

# asyncio run coroutine
asyncio.run(main())
