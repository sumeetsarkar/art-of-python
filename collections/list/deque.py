"""
Demonstrates deque

Double - Ended Queues

Though list objects support similar operations, they are optimized for fast fixed-length operations 
and incur O(n) memory movement costs for pop(0) and insert(0, v) operations 
which change both the size and position of the underlying data representation.

If maxlen is not specified or is None, deques may grow to an arbitrary length.

Otherwise, the deque is bounded to the specified maximum length.
Once a bounded length deque is full, when new items are added, 
a corresponding number of items are discarded from the opposite end. 
"""


from collections import deque


d = deque(['red', 'green', 'blue'], 6)

print(d)

# Adds to end of deque
d.append('cyan')
d.append('magenta')

# Adds to the begining of the deque
d.appendleft('yellow')

print(d)

# Since maxlen is 6, new addition on right using append, evicts 1 item from left (begining)
d.append('white')
print(d)
