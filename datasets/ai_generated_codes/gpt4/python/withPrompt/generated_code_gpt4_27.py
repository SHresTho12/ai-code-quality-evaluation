def flip_case(string: str) -> str:
    """Flip the case of each character in a string.

    Args:
    string (str): The input string.

    Returns:
    str: A new string with flipped case for each character.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()
