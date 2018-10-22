"""Debugging using pudb
"""

def add(a, b):
    import pudb; pudb.set_trace()
    # Stops the code before executing the next line
    # commands:
    #   n:  steps to next line
    #   s:  steps into the function
    #   b:  toggles breakpoint in line
    #   !:  switches context to interactive terminal
    #   Up/Down: to navigate code lines
    return a + b


add(2, 4)
