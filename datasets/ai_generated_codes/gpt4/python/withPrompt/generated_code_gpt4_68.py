def pluck(arr):
    """
    Pluck the node with the smallest even value.

    Args:
    arr (list): An array representing a branch of a tree with non-negative integer nodes.

    Returns:
    list: A list containing the smallest even value and its index. If no even values or the array is empty, return an empty list.

    Examples:
    >>> pluck([4, 2, 3])
    [2, 1]
    >>> pluck([1, 2, 3])
    [2, 1]
    >>> pluck([])
    []
    >>> pluck([5, 0, 3, 0, 4, 2])
    [0, 1]
    """
    smallest_even_value = float('inf')  # Initialize with positive infinity
    smallest_even_index = -1  # Initialize with -1 as there are no elements yet

    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even_value:
            smallest_even_value = arr[i]
            smallest_even_index = i

    if smallest_even_index != -1:
        return [smallest_even_value, smallest_even_index]
    else:
        return []
