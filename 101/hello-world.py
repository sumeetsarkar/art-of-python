"""
Welcome to python programming
Demonstrates a basic function and print to console
"""


def greet(name):
    """Function to greet a user with his name
    Parameters:
      name (str):
    """
    # print is inbuilt function to output to console
    # print invoked with 1 argument returns a string
    print('Hello ' + name)
    # print invoked with 2 or more arguments returns a tuple
    print('Hello', name)
    print('Hello', name)[1]
    # print('Hello', name)[2] # IndexError: tuple index out of range


# invoke greet function with arguments
greet('Sumeet')

# print the doc string for the file
print(__doc__)
