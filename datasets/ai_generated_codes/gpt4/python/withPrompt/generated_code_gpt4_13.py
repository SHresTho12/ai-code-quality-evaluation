def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.

    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a
