def median(l):
    """
    Calculate the median of elements in the list l.

    Args:
    l (list): The list of numbers.

    Returns:
    float: The median of the numbers in the list.

    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    n = len(sorted_l)

    if n % 2 == 1:
        # If the list has an odd length, return the middle element
        return sorted_l[n // 2]
    else:
        # If the list has an even length, return the average of the two middle elements
        middle1 = sorted_l[n // 2 - 1]
        middle2 = sorted_l[n // 2]
        return (middle1 + middle2) / 2.0

# Example tests
print(median([3, 1, 2, 4, 5]))          # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
