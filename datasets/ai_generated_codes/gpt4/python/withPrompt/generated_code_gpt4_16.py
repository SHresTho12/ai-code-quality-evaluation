def count_distinct_characters(string: str) -> int:
    """Count the number of distinct characters in a string, case-insensitive.

    Args:
    string (str): The input string.

    Returns:
    int: The number of distinct characters in the string.

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string.lower()))

