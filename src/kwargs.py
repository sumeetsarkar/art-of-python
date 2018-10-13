def print_arguments(**kwargs):
  for k,v in kwargs.items():
    print(k, v)

print_arguments(fname = 'Sumeet', lname = 'Sarkar')
# outputs
# fname Sumeet
# lname Sarkar

def print_arguments2(fname, **kwargs):
  for k,v in kwargs.items():
    print(k, v)

print_arguments2(fname = 'Sumeet', lname = 'Sarkar')
# outputs
# lname Sarkar