def get_positive(l: list) -> list:
    """Return only positive numbers from the list.

    Args:
    l (list): A list of numbers.

    Returns:
    list: A list containing only positive numbers from the original list.

    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in l if num > 0]
