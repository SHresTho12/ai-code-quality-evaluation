def common(l1: list, l2: list):
    """
    Returns a list of common elements between two lists.

    :param l1: The first list.
    :param l2: The second list.
    :return: A list containing elements that are common in both l1 and l2.
    """
    return list(set(l1) & set(l2))
