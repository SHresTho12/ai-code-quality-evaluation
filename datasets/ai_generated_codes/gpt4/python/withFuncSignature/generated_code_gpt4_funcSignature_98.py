def count_upper(s):
    """
    Counts the number of uppercase letters in a string.

    :param s: The string to be checked.
    :return: The count of uppercase letters in the string.
    """
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count
