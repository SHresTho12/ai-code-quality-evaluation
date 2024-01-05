import math


def poly(xs: list, x: float) -> float:
    """ Evaluates polynomial with coefficients xs at point x. """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def poly_derivative(xs: list, x: float) -> float:
    """ Evaluates the derivative of a polynomial with coefficients xs at point x. """
    return sum(i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0)

def find_zero(xs: list) -> float:
    """ Finds a root of the polynomial with coefficients xs using Newton's method. """
    if not xs:  # No coefficients, return an arbitrary root
        return 0

    x = 1  # Initial guess
    tolerance = 1e-6  # Tolerance for convergence
    max_iterations = 1000  # Maximum number of iterations
    for _ in range(max_iterations):
        y = poly(xs, x)
        y_prime = poly_derivative(xs, x)

        # Avoid division by zero in derivative
        if y_prime == 0:
            return x

        x_new = x - y / y_prime

        # Check for convergence
        if abs(x_new - x) < tolerance:
            return x_new

        x = x_new

    # If no convergence, return the last approximation
    return x

# Example usage
coefficients = [1, -3, 2]  # Represents x^2 - 3x + 2
root = find_zero(coefficients)
root

METADATA = {}

def check(find_zero):
    import math
    import random
    rng = random.Random(42)
    import copy

    for _ in range(100):
        ncoeff = 2 * rng.randint(1, 4)
        coeffs = []
        
        for _ in range(ncoeff):
            coeff = rng.randint(-10, 10)
            if coeff == 0:
                coeff = 1
            coeffs.append(coeff)

        solution = find_zero(copy.deepcopy(coeffs))
        assert math.fabs(poly(coeffs, solution)) < 1e-4

check(find_zero)