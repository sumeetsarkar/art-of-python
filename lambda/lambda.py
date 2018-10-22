def multiplier(num):
    return lambda a: a * num


twice = multiplier(2)
thrice = multiplier(3)

print(twice(4))
print(thrice(4))

list = [1, 2, 3, 4, 5]

result = map(lambda n: n * 2, list)
for x in result:
    print(x)

for n in list:
    print((lambda a: a * 2)(n))

result = filter(lambda n: n % 2 == 0, list)
for x in result:
    print(x)

print((lambda a, b: a * b * 10)(10, 20))
