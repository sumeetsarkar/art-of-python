"""Debugging using web_pdb
"""

def add(a, b):
    import web_pdb; web_pdb.set_trace()

    # OR, use breakpoint() using PYTHONBREAKPOINT
    # PYTHONBREAKPOINT='web_pdb.set_trace' python3 debug_web_pdb.py
    breakpoint()

    # Stops the code before executing the next line
    # Open http://localhost:5555
    return a + b


add(2, 4)
