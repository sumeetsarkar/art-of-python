# Tuple

Tuple is an ordered and immutable collection of items.

Being immutable, iterating through tuple is much faster than with list and is encouraged to use write protected data.

Also, tuples with immutable elements can be used as key for a dictionary, but not possible with list. See the Example of tuple used as key in a dict in [Fibonacci with memoization](https://github.com/sumeetsarkar/art-of-python/blob/9e85b9bfd83752d63f7d38597f0244322e9b379d/decorators/memoisation.py#L36)


```python
# Tuple assingment
justTuple = 1, 2, 3, 4, 4, 5, 6
print(justTuple)

# Tuple count function returns the number of occurences of given item
print('Tuple count of 2:', justTuple.count(2))
print('Tuple count of 4:', justTuple.count(4))
print('Tuple count of 0:', justTuple.count(0))

# index() Returns the first index of occurence of given item
print('Index of 2:', justTuple.index(2))
print('Index of 4:', justTuple.index(4))
# print('Index of 0:', justTuple.index(0))    # raises ValueError: 0 not in tuple

```

## Tuple Packing Unpacking

Tuple can be unpacked to individual variables

__Note:__ number of explicit variables to unpack a tuple, should be equal to the tuple length


If there are n variables unpacking a tuple, then following ```ValueError``` may be raised in scenarios of:

m variables to unpack, where m < tuple length: ValueError: too many values to unpack (expected n)

m variables to unpack, where m > tuple length: ValueError: not enough values to unpack (expected m, got n)


```python
# Tuple unpack
tu1, tu2, tu3, tu4 = 1, 2, 3, 4
print(tu1, tu2, tu3, tu4)
```


## Tuples are iterarables

```python
# Tuple iteration
for n in justTuple:
    print(n)
```


## Swaping item values in tuples

```python
x = 10
y = 20

y, x = x, y
```
