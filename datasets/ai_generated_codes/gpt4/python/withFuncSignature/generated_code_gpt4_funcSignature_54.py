def same_chars(s0: str, s1: str):
    """
    Checks if two strings consist of the same characters, irrespective of order or frequency.

    :param s0: The first input string.
    :param s1: The second input string.
    :return: True if both strings have the same set of characters, False otherwise.
    """
    return set(s0) == set(s1)
