"""Demonstrates python lists
    
    Following dict methods are illustrated
        all
        any
        append
        clear
        copy
        extend
        index
        len
        remove
        reverse
        sort
"""

colors = ['red', 'green', 'blue']

# Adds new item to the last of the colors
colors.append('white')
print(colors)

# Concatenates the colors provided in argument
colors.extend(['cyan', 'magenta', 'yellow'])
print(colors)

# Returns the first index of the found item
print(colors.index('cyan'))
# Scans the colors from index 4
print(colors.index('cyan', 4))
# Scans the colors from index 0 to 4
print(colors.index('cyan', 0, 5))
# print(colors.index('some color')) # ValueError: 'some color' is not in colors

# Removes item with specific value
colors.remove('white')
print(colors)

# Makes a copy of the colors and returns new colors
list_copy = colors.copy()
print(colors)
print(list_copy)

# Reverses the colors
list_copy.reverse()
print(list_copy)

# Sorts the colors
list_copy.sort()
print(list_copy)

# Empties all the items in the colors
list_copy.clear()
print(colors)
print(list_copy)

# Prints length of colors
print(len(colors))

# Returns True if any item in an iterable object is true
print(any(colors))

# Returns True if all items in an iterable object are true
print(all(colors))
