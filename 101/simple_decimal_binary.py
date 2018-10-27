"""
Simple program to convert between binary and decimal
"""

def decimaltobinary(d):
    binary = []
    while d/2 != 0:
        d, r = divmod(d, 2)
        binary.append(str(r))
    binary.reverse()
    return int(''.join(binary))
    

def binarytodecimal(b):
    a = [s for s in str(b)]
    a.reverse()
    d = 0
    for i in range(len(a)):
        d += 2**i * int(a[i])
    return d


print(decimaltobinary(49))      # 110001
print(binarytodecimal(110001))  # 49

print(binarytodecimal(decimaltobinary(49)) == 49)   # True
