"""Demonstrates python dictionaries
    
    Following dict methods are illustrated
        clear
        copy
        fromkeys
        get
        items
        keys
        pop
        popitem
        update
        values
"""

# declaring a dictionary
colordict = {'r':'RED', 'g':'GREEN', 'b':'BLUE'}
print(colordict)

# using dict
colordict = dict(r='RED', g='GREEN', b='BLUE')
print(colordict)


def print_keys(dict):
    print('\nprinting keys...')
    for k in dict.keys():
        print(k)


def print_values(dict):
    print('\nprinting values...')
    for k in dict.values():
        print(k)


def dict_traversal(dict):
    print('\ndict traversal...')
    for k, v in dict.items():
        print(k, v)


def build_person(name, age, city):
    person = {
        'name': name,
        'age': age,
    }
    address = {
        'city': city,
    }
    person['address'] = address
    return person


def print_person(person):
    print('\nprint person object')
    address = person.get('address', {})
    print(person['name'], person['age'], 'lives in', address.get('city', 'unkown'))


def get_rgb_map():
    return {
        0: 'RED',
        1: 'GREEN',
        2: 'BLUE',
    }

person = build_person('Sumeet Sarkar', 28, 'Bangalore')
print_person(person)

rgb_map = get_rgb_map()
print_keys(rgb_map)
print_values(rgb_map)
dict_traversal(rgb_map)

print(rgb_map.pop(0, 'Unkown color'))   # key 0 is removed
# print(rgb_map.pop(3))     # raises KeyError: 3 as key is not present in dict and no default value is passed
print(rgb_map.pop(3, 'Unkown color'))   # even though key 3 is not present, default value saves the KeyError

dict_traversal(rgb_map)

# Adding 0: RED again
rgb_map[0] = 'RED'

dict_traversal(rgb_map)

# Removes an arbitrary
rgb_map.popitem()

# Pop all items unless size of dict is 0
while len(rgb_map) > 0:
    rgb_map.popitem()   # popitem if called on empty dict, raises KeyError:

dict_traversal(rgb_map)

# Get new map
rgb_map = get_rgb_map()
dict_traversal(rgb_map)

# update() accepts a dictionary 
# if K exists in the dict the method is called upon: then V for K is updated
# else new K, V is added
rgb_map.update({2: 'VERY VERY BLUE'})
rgb_map.update({3: 'HYBRID'})
# In essence update can be used to merge two dicts corresponding to Ks
rgb_map.update({4: 'SOME COLOR', 5: 'REALLY WHITE'})
dict_traversal(rgb_map)


# copy() method returns a shallow copy of the dictionary
rgb_map_clone = rgb_map.copy()

# Clears the dict
rgb_map_clone.clear()

dict_traversal(rgb_map_clone)
dict_traversal(rgb_map)

rgb_map_clone = rgb_map
# here, clear() empties both rgb_map_clone & rgb_map
rgb_map_clone.clear()

dict_traversal(rgb_map_clone)
dict_traversal(rgb_map)


# string is split into individual chars for keys
vowel_dict = dict.fromkeys('aeiou', None)
vowel_dict = dict.fromkeys('aeiou')     # value param if not passed, defaults to None
dict_traversal(vowel_dict)

# or pass it an array, which is mostly practical
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_dict = dict.fromkeys(vowels)
dict_traversal(vowel_dict)


# Pass in optional V param to be associated with each K
vowel_dict = dict.fromkeys(vowels, person)
dict_traversal(vowel_dict)

# Since, fromkeys V param is an object passed as reference to each key
# Changing the V, updates the V in all
person.update({'name': 'Sumeet'})
dict_traversal(vowel_dict)


# Destructuring a dictionary
rgbcolors = {'r':'RED', 'g':'GREEN', 'b':'BLUE'}
r, g, b = [rgbcolors[k] for k in rgbcolors.keys()]

print('\ndict destructuring...')
print(r, g, b)


# Print the dictionary items in the sorted order of keys
for k in sorted(rgbcolors.keys()):
    print(k, rgbcolors[k])
