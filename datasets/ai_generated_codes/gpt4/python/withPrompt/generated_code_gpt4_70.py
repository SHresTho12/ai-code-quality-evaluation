def strange_sort_list(lst):
    """
    Return a list sorted in a strange order, starting with the minimum value,
    then the maximum of the remaining integers, then minimum, and so on.

    Args:
    lst (list): A list of integers.

    Returns:
    list: The list sorted in a strange order.

    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """
    result = []  # Initialize the result list

    while lst:
        min_val = min(lst)  # Find the minimum value in the remaining list
        result.append(min_val)  # Add it to the result
        lst.remove(min_val)  # Remove the minimum value from the list

        if lst:  # Check if there are remaining elements in the list
            max_val = max(lst)  # Find the maximum value in the remaining list
            result.append(max_val)  # Add it to the result
            lst.remove(max_val)  # Remove the maximum value from the list

    return result
