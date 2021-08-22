def fact(n):
    """Return Factorial of N"""
    # Base case is 1
    if n == 1:
        return 1
    # Alternate creates a new scope
    else:
        return n*fact(n-1)