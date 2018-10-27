"""
Demonstrates Counter in collections
"""


from collections import Counter


# A sample string
string = 'A quick brown fox jumps over a lazy dog'

# Initialize the Counter object
countchars = Counter()

for c in string.replace(' ', ''):
    # Increase count for each char
    countchars[c] = countchars[c] + 1

# Prints the character frequency
for k, v in countchars.items():
    print(k, v)
