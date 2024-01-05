def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base.

    Args:
    x (int): The input number to be converted.
    base (int): The target numerical base (less than 10).

    Returns:
    str: The string representation of the number after the conversion.

    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9 (inclusive)")

    if x == 0:
        return '0'  # Special case for x = 0

    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x //= base

    return result

# Example tests
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
