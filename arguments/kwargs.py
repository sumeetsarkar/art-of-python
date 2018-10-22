def print_arguments(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


print_arguments()  # no output

print_arguments(fname='Sumeet', lname='Sarkar')
# outputs
# fname Sumeet
# lname Sarkar


def print_arguments2(fname, **kwargs):
    for k, v in kwargs.items():
        print(k, v)


print_arguments2(fname='Sumeet', lname='Sarkar')
# outputs
# lname Sarkar


def print_arguments3(fname, *args, **kwargs):
    print(args)
    for k, v in kwargs.items():
        print(k, v)

# print_arguments3(fname = 'Sumeet', 'hello', lname = 'Sarkar') # positional arguments follows argument

# print_arguments3('hello', fname = 'Sumeet', lname = 'Sarkar') # still invalid as fname is a named recieving argument


# fname recieves 'Sumeet', and kwargs recieve lname
print_arguments3('Sumeet', lname='Sarkar')
# fname recieves 'Sumeet', args recieve hello and kwargs recieve lname
print_arguments3('Sumeet', 'hello', lname='Sarkar')
