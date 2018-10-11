person = {
  'name': 'Sumeet Sarkar',
  'age': 28,
}

address = {
  'city': 'Bangalore',
}

person['address'] = address

def printPerson(name = 'someone', age = '0', address = {}):
  print(name, age, 'lives in', address.get('city'))

printPerson()
printPerson(person['name'])
printPerson(person['name'], person['age'])
printPerson(person['name'], person['age'], person['address'])

printPerson(
  address = person['address'],
  age = person['age'],
  name = person['name'],
)
