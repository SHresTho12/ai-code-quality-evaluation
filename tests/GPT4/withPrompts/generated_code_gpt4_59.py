def largest_prime_factor(n: int):
    """
    Return the largest prime factor of the given integer n.

    Args:
    n (int): The integer for which the largest prime factor is to be found.

    Returns:
    int: The largest prime factor of n.

    Examples:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find and store the smallest prime factor
    smallest_prime = 2
    while n > 1:
        if n % smallest_prime == 0:
            n //= smallest_prime
        else:
            smallest_prime += 1
    return smallest_prime

# Example tests
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
METADATA = {}

def check(largest_prime_factor):
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(63) == 7
    assert largest_prime_factor(330) == 11
    assert largest_prime_factor(13195) == 29

check(largest_prime_factor)