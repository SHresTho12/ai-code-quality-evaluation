def next_smallest(lst):
    """
    Replaces each element in the list with the next smallest element in the list.
    If there is no smaller element, the value is replaced with -1.

    :param lst: A list of integers.
    :return: A new list with each element replaced by the next smallest element.
    """
    result = []
    for i in range(len(lst)):
        next_smaller = -1  # Default value if no smaller element is found
        for j in range(len(lst)):
            if lst[j] < lst[i]:
                # Check if this is the first smaller element found or if it's smaller than the current next_smaller
                if next_smaller == -1 or lst[j] > next_smaller:
                    next_smaller = lst[j]
        result.append(next_smaller)
    return result
