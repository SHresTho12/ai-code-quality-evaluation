def total_match(lst1, lst2):
    """
    Counts the total number of matching elements between two lists.

    :param lst1: The first list.
    :param lst2: The second list.
    :return: The total count of matching elements.
    """
    count = 0
    for element in lst1:
        if element in lst2:
            count += 1
    return count
