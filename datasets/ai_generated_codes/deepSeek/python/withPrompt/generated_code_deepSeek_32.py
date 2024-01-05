import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    # The derivative of a polynomial is a polynomial of one degree less.
    # We calculate the derivative of the polynomial and find its root.
    derivative = [i * coeff for i, coeff in enumerate(xs)][1:]
    # We use the Newton-Raphson method to find the root of the derivative.
    x = 0.0
    while abs(poly(derivative, x)) > 1e-6:
        x = x - poly(xs, x) / poly(derivative, x)
    return x