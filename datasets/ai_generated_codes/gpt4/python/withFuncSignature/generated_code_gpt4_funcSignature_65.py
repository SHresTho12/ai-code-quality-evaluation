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
