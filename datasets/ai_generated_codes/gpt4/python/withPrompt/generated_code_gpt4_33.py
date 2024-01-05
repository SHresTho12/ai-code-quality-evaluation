def sort_third(l: list) -> list:
    """Sort elements at indices divisible by three in a list, keeping other elements in their original positions.

    Args:
    l (list): The input list.

    Returns:
    list: The modified list with specified elements sorted.

    Examples:
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # Extract elements at indices divisible by three
    third_elements = [l[i] for i in range(len(l)) if (i + 1) % 3 == 0]
    third_elements.sort()

    # Reinsert the sorted elements back into their positions
    j = 0
    for i in range(len(l)):
        if (i + 1) % 3 == 0:
            l[i] = third_elements[j]
            j += 1

    return l
