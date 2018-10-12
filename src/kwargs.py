def printArguments(**kwargs):
  for k,v in kwargs.items():
    print(k, v)

printArguments(fname = 'Sumeet', lname = 'Sarkar')
# outputs
# fname Sumeet
# lname Sarkar

def printArguments2(fname, **kwargs):
  for k,v in kwargs.items():
    print(k, v)

printArguments2(fname = 'Sumeet', lname = 'Sarkar')
# outputs
# lname Sarkar