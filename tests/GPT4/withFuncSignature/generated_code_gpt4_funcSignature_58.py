def common(l1: list, l2: list):
    """
    Returns a list of common elements between two lists.

    :param l1: The first list.
    :param l2: The second list.
    :return: A list containing elements that are common in both l1 and l2.
    """
    return list(set(l1) & set(l2))


METADATA = {}

def check(common):
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert common([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert common([4, 3, 2, 8], []) == []

check(common)
