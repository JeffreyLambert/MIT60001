"""
Purpose: Implement the Newton-Raphson algorithm for
    finding the root of a function
"""


def find_root(func, gradient, x0=0, epsilon=0.0001, learning_rate=1):
    """
    Find the root of a function using a Newton-Raphson method
    Args:
        func: Function to be evaluated
        gradient: First derivative of the function to be evaluated
        x0: initial value of root
        epsilon: precision of gradient evaluated at x with respect to 0
        learning_rate: augments the step size for each iteration

    Returns:
        x: root of the function
        i: iterations required to converge

    """
    x = x0
    iterations = 0
    while abs(gradient(x) - 0) > epsilon:
        iterations += 1
        step = func(x) / gradient(x)
        x -= learning_rate * step
    return x, i
