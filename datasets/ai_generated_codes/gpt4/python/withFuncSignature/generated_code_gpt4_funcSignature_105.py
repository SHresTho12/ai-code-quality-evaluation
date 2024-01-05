def by_length(arr):
    """
    Sorts a list of strings based on their lengths in ascending order.

    :param arr: The list of strings to be sorted.
    :return: The sorted list of strings.
    """
    return sorted(arr, key=len)
