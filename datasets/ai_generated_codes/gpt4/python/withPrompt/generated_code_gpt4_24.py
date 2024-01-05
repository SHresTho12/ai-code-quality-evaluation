def largest_divisor(n: int) -> int:
    """Find the largest number smaller than n that divides n evenly.

    Args:
    n (int): The number for which to find the largest divisor.

    Returns:
    int: The largest divisor of n smaller than n itself.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

    return 1  # This line is redundant as n is at least 2 and 1 will always be a divisor
