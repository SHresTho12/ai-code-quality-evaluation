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
METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(factorize): 
    assert factorize(2) == [2] 
    assert factorize(4) == [2, 2] 
    assert factorize(8) == [2, 2, 2] 
    assert factorize(3 * 19) == [3, 19] 
    assert factorize(3 * 19 * 3 * 19) == [3, 3, 19, 19] 
    assert factorize(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19] 
    assert factorize(3 * 19 * 19 * 19) == [3, 19, 19, 19] 
    assert factorize(3 * 2 * 3) == [2, 3, 3] 
    
check(factorize)