def modp(n, p):
    """
    Calculate 2^n modulo p.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.

    Example:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = pow(2, n, p)
    return result

# Example tests
print(modp(3, 5))       # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))     # Output: 1
print(modp(3, 11))      # Output: 8
print(modp(100, 101))   # Output: 1

METADATA = {}

def check(modp):
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
    assert modp(30, 5) == 4
    assert modp(31, 5) == 3

check(modp)