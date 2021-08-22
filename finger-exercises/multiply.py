"""
Purpose: Create multiplication function
    which demonstrates recursion in Python
"""


def mult(a, b):
    """
    Add a together b times
    Args:
        a: integer 1
        b: integer 2

    Returns: int, product of a and b

    """
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)