"""
Demonstrates chain map

Combines multiple dictionary into single dictionary for lookups

A ChainMap incorporates the underlying mappings by reference.
So, if one of the underlying mappings gets updated, those changes will be reflected in ChainMap.
"""


from collections import ChainMap


rgb = {'r':'RED', 'g':'GREEN', 'b':'BLUE'}
cmy = {'c':'CYAN', 'm':'MAGENTA', 'y':'YELLOW'}
random = {'w': 'WHITE', 'r': 'TRUELY RED'}
random2 = {'r':'TRUELY RED 2'}

colormap = ChainMap(rgb, cmy, random, random2)

print([k for k in colormap.keys()])
print([v for v in colormap.values()])
print([maps for maps in colormap.maps])

print(colormap.get('c'))    # CYAN
print(colormap.get('r'))    # RED
# print(colormap['d'])    # raises KeyError

# parents skips the first map from current instance
# Here, colormap.parents infers only cmy, random, random2
print(colormap.parents.get('r'))    # TRUELY RED

# Here, colormap.parents.parents.parents infers only random2
print(colormap.parents.parents.parents.get('r'))    # TRUELY RED 2

# Here, colormap.parents.parents.parents infers empty map! {}
print(colormap.parents.parents.parents.parents.get('r'))    # None

# Updating the child map will update the ChainMap
# As ChainMap incorporates the underlying mappings by reference.
rgb['b'] = 'VERY BLUE'
print(colormap['b'])


print('Print all K,V pair using ChainMap maps method')
# Print each k, v in ChainMap
for map in [maps for maps in colormap.maps]:
    for k, v in map.items():
        print(k, v)
