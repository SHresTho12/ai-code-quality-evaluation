def circular_shift(x, shift):
    """
    Performs a circular shift on a list by a specified number of positions.

    :param x: The list to be shifted.
    :param shift: The number of positions to shift the list by. 
                  A positive value shifts to the right, and a negative value shifts to the left.
    :return: The shifted list.
    """
    if not x:  # Check for empty list
        return x

    n = len(x)
    shift = shift % n  # Handle shifts larger than the list size
    return x[-shift:] + x[:-shift]


def check(circular_shift):
    # Check some simple cases
    assert circular_shift(100, 2) == "001"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(97, 8) == "79"
    assert circular_shift(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert circular_shift(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"

check(circular_shift)