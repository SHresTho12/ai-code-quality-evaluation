from typing import List

def factorize(n: int) -> List[int]:
    """Return a list of prime factors of a given integer.

    Args:
    n (int): The integer to factorize.

    Returns:
    List[int]: A list of prime factors, each listed the number of times it appears in the factorization.

    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors
