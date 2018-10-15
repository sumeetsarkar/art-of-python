"""
Demonstrates use cases of generators
"""

import time

def compute():
  for x in range(5):
    time.sleep(.5)
    yield x

# directly calling a function implementing yield inside will return generator object
val = compute()
print(val)  # prints generator object

# generator methods can be iterated over
for val in compute():
  print(val)

# get an iterator and iterate over
val = iter(compute())
while True:
  try:
    print(val.next())
  except StopIteration:
    break
