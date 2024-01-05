def fizz_buzz(n: int) -> int:
    """Count the number of times the digit 7 appears in integers less than n that are divisible by 11 or 13.

    Args:
    n (int): The upper limit (exclusive).

    Returns:
    int: The count of digit 7 appearances in qualifying numbers.

    Examples:
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count
