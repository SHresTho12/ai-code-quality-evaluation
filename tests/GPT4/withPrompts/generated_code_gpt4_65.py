def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shifting the digits right by shift
    and return the result as a string.
    If shift is greater than the number of digits, return the digits reversed.

    Args:
    x (int): The input integer.
    shift (int): The number of positions to shift the digits.

    Returns:
    str: The result after circular shifting.

    Examples:
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    >>> circular_shift(12345, 3)
    '34512'
    >>> circular_shift(12345, 6)
    '54321'
    """
    x_str = str(x)
    num_digits = len(x_str)

    # Calculate the effective shift by taking the remainder when dividing by num_digits
    effective_shift = shift % num_digits

    # Perform circular shift by slicing the string and reordering
    result = x_str[-effective_shift:] + x_str[:-effective_shift]

    return result
def check(circular_shift):
    # Check some simple cases
    assert circular_shift(100, 2) == "001"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(97, 8) == "79"
    assert circular_shift(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert circular_shift(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"

check(circular_shift)