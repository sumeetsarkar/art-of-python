"""
Demonstrates Counter in collections

A Counter is a dict subclass for counting hashable objects. 
It is an unordered collection where elements are stored as dictionary keys 
and their counts are stored as dictionary values. 

Counts are allowed to be any integer value including zero or negative counts
"""


from collections import Counter


# A sample string
string = 'A quick brown fox jumps over a lazy dog'

# Initialize the Counter object with a string iterable
countchars = Counter(string.replace(' ', ''))

# Prints the character frequency
for k, v in countchars.items():
    print(k, v)


# Initialize the Counter object with a list iterable
countcolors = Counter(['RED', 'GREEN', 'BLUE', 'RED'])
print(countcolors)
print(countcolors['RED1'])  # Does not raise KeyError if key not found, instead prints occurence count to 0


# Initialize the Counter object with dict
countcolors = Counter({'red': 4, 'blue': 2})
print(countcolors)

# Returns top 3 common
print(countchars.most_common(3))
# Returns full set
print(countchars.most_common())


# Update - element counts are added
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4, e=5)
c.update(d)
print(c)


# Subtract - element counts are subtracted
c = Counter(a=4, b=2, c=0, d=10)
d = Counter(a=1, b=2, c=3, d=4, e=5)
c.subtract(d)
print(c)

# prints elements as per frequeny of appearence (freq > 0)
print([i for i in c.elements()])
