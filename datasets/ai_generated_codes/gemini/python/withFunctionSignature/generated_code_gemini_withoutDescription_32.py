
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of the polynomial xs using Brent's method.

    Args:
        xs: A list of coefficients of the polynomial.

    Returns:
        A float representing a zero of the polynomial, or None if no zero is found.
    """

    a, b, c = 0, 1, 2
    fa, fb, fc = poly(xs, a), poly(xs, b), poly(xs, c)
    while abs(fb) > 1e-10:
        if (fa * fc) > 0:
            a, b = b, c
            fa, fb, fc = fb, fc, poly(xs, c)
        else:
            d = (b - a) / (fc - fb)
            e = fb + d * (fc - fb)
            if abs(e) < abs(fb):
                a, b = b, a
                fa, fb = fb, e
            else:
                c = b
                b = b + d
                fc = poly(xs, c)
    return (a + b) / 2

