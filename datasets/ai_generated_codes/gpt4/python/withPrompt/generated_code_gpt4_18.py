def how_many_times(string: str, substring: str) -> int:
    """Count how many times a substring occurs in a string, including overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to count in the original string.

    Returns:
    int: The number of times the substring occurs in the string.

    Examples:
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        return 0

    count = 0
    start = 0

    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1

    return count
