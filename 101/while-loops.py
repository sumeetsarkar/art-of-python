"""
Demostrates different types of for loops
"""

num = 5
while num is not 0:     # could also be, while num != 0:
    print('num is', num)
    num -= 1

colors = ['red', 'green', 'blue', 'red', 'yellow', 'blue']
n = 0
while True:
    if colors[n] is 'yellow':
        # break while loop interation if yellow is found
        break
    else:
        # else increment the index and continue
        n += 1
        continue  # continue here is optional

print('position of yellow', n)
