def printColors(*colors):
    for color in colors:
        if type(color) is dict:
            print(color.get('key'), color.get('name'))
        else:
            print(color)


printColors()  # no output

printColors('voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red')

printColors(
    {'key': 0, 'name': 'voilet'},
    {'key': 1, 'name': 'indigo'},
    {'key': 2, 'name': 'blue'},
    {'key': 3, 'name': 'green'},
    {'key': 4, 'name': 'yellow'},
    {'key': 5, 'name': 'orange'},
    {'key': 6, 'name': 'red'},
)
