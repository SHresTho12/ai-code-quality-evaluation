def derivative(xs: list):
    """
    Compute the derivative of a polynomial represented by its coefficients.

    Args:
    xs (list): List of coefficients of the polynomial, where xs[0] is the coefficient of x^0, xs[1] is the coefficient of x^1, and so on.

    Returns:
    list: List of coefficients of the derivative polynomial.

    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    derivative_coeffs = []
    for i in range(1, len(xs)):
        derivative_coeffs.append(i * xs[i])
    return derivative_coeffs

# Example tests
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))        # Output: [2, 6]
METADATA = {}

def check(derivative):
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([3, 2, 1]) == [2, 2]
    assert derivative([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert derivative([1]) == []

check(derivative)