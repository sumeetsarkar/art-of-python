"""
Demonstrates Ordered dict

An OrderedDict is a dict that remembers the order that keys were first inserted.
If a new entry overwrites an existing entry, the original insertion position is left unchanged. 
Deleting an entry and reinserting it will move it to the end.
"""


from collections import OrderedDict


od = OrderedDict(red='RED', green='GREEN', blue='BLUE')

od['cyan'] = 'CYAN'
od['magenta'] = 'MAGENTA'
od['yellow'] = 'YELLOW'

# Ordered output, as per the order of entry
print(od)

od.pop('red')
# Pop key and renter k, v pair will re-insert pair in end
od['red'] = 'RED'
print(od)


# Updates to existing k,v will not alter the position
od['cyan'] = 'Cyan'
print(od)


# Always pops from the last
od.popitem(last=True)
print(od)


# The item is moved to the right end if last is true (the default) or to the beginning if last is false.
# Raises KeyError if the key does not exist
# Default is last=True
od.move_to_end('cyan')
print(od)

od.move_to_end('cyan', last=False)
print(od)
