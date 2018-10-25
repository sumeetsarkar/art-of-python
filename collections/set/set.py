"""Demonstrates python set

    Following dict methods are illustrated
        add
        clear
        copy
        difference
        difference_update
        discard
        intersection
        intersection_update
        isdisjoint
        issubset
        issuperset
        pop
        remove
        symmetric_difference
        symmetric_difference_update
        union
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

# Few set operations
numberset1 = {1, 2, 3, 4, 5}
numberset2 = {1, 2, 3, 4, 5, 7, 9}

# Intersection of set
print(numberset1.intersection(numberset2))

# Union of set
print(numberset1.union(numberset2))

# Disjoint check, checks for exclusivity of items in set
print(numberset1.isdisjoint(numberset2))

# Checks if numberset1 is subset of numberset2
print(numberset1.issubset(numberset2))

# Checks if numberset1 is superset of numberset2
print(numberset1.issuperset(numberset2))
print(numberset2.issuperset(numberset1))

# Updates a set with intersection of another sets 
numberset1.intersection_update(numberset2, numberset2, {1, 10, 20, 30, 40, 50})
# numberset1 now has the smallest intersection items
print(numberset1)
print(numberset2)


numberset1 = {1, 2, 3, 4, 5, 7, 9}
numberset2 = {1, 2, 3, 4, 5}

# Returns a set that contains the items that only exist in set x, and not in set y
print(numberset1.difference(numberset2))

# Updates the numberset1 with difference with numberset2
numberset1.difference_update(numberset2)
print(numberset1)


numberset1 = {1, 2, 3, 4, 5, 7, 9}
numberset2 = {1, 2, 3, 4, 5, 8, 10}

# Returns a set the contains disjoint items from both sets,
# unlike difference, which only returns disjoints from the set the function is called upon
print(numberset1.symmetric_difference(numberset2))

# Updates the numberset1 with symmetric_difference with numberset2
numberset1.symmetric_difference_update(numberset2)
print(numberset1)
