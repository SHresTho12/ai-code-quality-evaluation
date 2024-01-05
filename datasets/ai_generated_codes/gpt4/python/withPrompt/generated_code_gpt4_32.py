import math

def poly(xs: list, x: float):
    """
    Evaluates a polynomial with coefficients xs at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def derivative(xs: list, x: float):
    """
    Computes the derivative of the polynomial at point x.
    """
    return sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs) if i > 0])

def find_zero(xs: list) -> float:
    """
    Finds a zero point of the polynomial with coefficients xs.
    """
    if len(xs) % 2 != 0 or all(coeff == 0 for coeff in xs):
        raise ValueError("List must have an even number of coefficients and a non-zero coefficient")

    # Initial guess
    x0 = 0.0
    for _ in range(1000):  # Limit iterations to avoid infinite loops
        y = poly(xs, x0)
        y_prime = derivative(xs, x0)

        if y_prime == 0:  # Avoid division by zero
            return x0

        x1 = x0 - y / y_prime
        if abs(x1 - x0) < 1e-6:  # Check for convergence
            return x1
        x0 = x1

   
