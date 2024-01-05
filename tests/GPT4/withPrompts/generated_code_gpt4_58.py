def common(l1: list, l2: list):
    """
    Return a sorted list of unique common elements between two lists.

    Args:
    l1 (list): The first list.
    l2 (list): The second list.

    Returns:
    list: A sorted list of unique common elements.

    Examples:
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    set1 = set(l1)
    set2 = set(l2)
    common_elements = set1.intersection(set2)
    return sorted(list(common_elements))

# Example tests
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))                               # Output: [2, 3]
METADATA = {}

def check(common):
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert common([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert common([4, 3, 2, 8], []) == []

check(common)
