def derivative(xs: list):
    """
    Calculates the derivative of a polynomial represented by a list of coefficients.
    The list index corresponds to the power of x, e.g., [3, 2, 1] represents 3 + 2x + x^2.

    :param xs: A list of coefficients representing a polynomial.
    :return: A list of coefficients representing the derivative of the polynomial.
    """
    if not xs:  # Check for an empty list
        return []

    # The derivative of a constant (degree 0 polynomial) is 0
    if len(xs) == 1:
        return [0]

    # Calculate the derivative
    return [i * xs[i] for i in range(1, len(xs))]


METADATA = {}

def check(derivative):
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([3, 2, 1]) == [2, 2]
    assert derivative([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert derivative([1]) == []

check(derivative)