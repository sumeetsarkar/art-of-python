"""Debugging using pdb
"""

def add(a, b):
    import pdb; pdb.set_trace()

    # OR, use breakpoint()
    breakpoint()
    
    # Stops the code before executing the next line
    # commands:
    #   next:   steps to next line
    #   step:   steps into the function
    #   cont:   continues execution from breakpoint
    return a + b


add(2, 4)
