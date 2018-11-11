"""Demonstrates python lists
    
    Following dict methods are illustrated
        all
        any
        append
        clear
        copy
        count
        extend
        index
        len
        remove
        reverse
        sort
"""

colors = ['red', 'green', 'blue']

# List is iterable
for c in colors:
    print(c)

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

# Count the number of items in array with specified Value
print(colors.count('yellow'))

# Sorting with Key

# Simple use case, key=len
myarr = ['aa', 'a', 'aaaa', 'aaa']
myarr.sort(key=len)
print(myarr)
myarr.sort(key=len, reverse=True)   # reverese indicates to reverese the order decided by key
print(myarr)


# Complex use case, key= custom function
def sort_func(e):
    """Get the maximum length of string, for all values in dict
    """
    return max(e.values(), key=len)

listdict = [
    {0:'RED', 1:'GREEN', 2:'BLUE'},
    {0:'CYAN', 1:'MAGENTA', 2:'YELLOW'},
    {0:'A', 1:'BB'},
]

listdict.sort(key=sort_func, reverse=True)
print(listdict)

# Pop, pops the element at given index
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow']
print(colors)
# Removes first item
colors.pop(0)
print(colors)
# Removes last item
colors.pop(-1)
print(colors)
colors.pop()
# No index, removes last time
print(colors)

# Initialize a list of size 1 with element as 0 
nums = [0]
print('\nArray size 1\n', nums)

# Initialize a list of size 10 with each element as 0
nums = [0] * 10
print('\nArray size 10\n', nums)

# Intialize a 2D list of 10, 10 size with each element as 0
nums2d = [[0] * 10] * 10
print('\n2D Array size 10, 10, each element 0\n', nums2d)

# Generate a 2D list 10, 10 size with numbers in each list from 0-9
nums2d = [[i for i in range(10)] for _ in range(10)]
print('\n\n2D Array size 10, 10, 0-9\n', nums2d)

# Same as above
nums2d = [[i for i in range(10)]] * 10
print('\n\n2D Array size 10, 10, 0-9\n', nums2d)

# Generate a Array with numbers from 0-9 repeating 10 times
nums2d = [i for i in range(10)] * 10
print('\n\nArray size 100 repeating 0-9\n', nums2d)
