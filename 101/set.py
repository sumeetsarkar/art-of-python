"""Demonstrates python set

    Following dict methods are illustrated
    add
    clear
    copy
    discard
    pop
    remove
    updated
"""

colors = {'red', 'green', 'blue'}

print(colors)

# Set is iterable
for c in colors:
    print(c)

# in relationship
print('red' in colors)

# Length of a set
print(len(colors))

# Add item in set
colors.add('white')
print(colors)

# Extend a set with an array of items
colors.update(['cyan', 'magenta', 'yellow'])
# Order is not preserved
print(colors)

colors.remove('yellow')
# colors.remove('yellow') # raises KeyError: 'yellow' not present

colors.discard('yellow')  # silent even if key not present
print(colors)

# Arbitrary item is poped
colors.pop()
print(colors)

# Copy the set
colors_copy = colors.copy()
print(colors_copy)

# Clear the set
colors_copy.clear()
print(colors_copy)