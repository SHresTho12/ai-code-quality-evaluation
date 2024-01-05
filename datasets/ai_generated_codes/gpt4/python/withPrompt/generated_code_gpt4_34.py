def unique(l: list) -> list:
    """Return sorted unique elements from the list.

    Args:
    l (list): The input list.

    Returns:
    list: A sorted list of unique elements from the input list.

    Examples:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))
