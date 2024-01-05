def count_nums(arr):
    """
    Counts the number of numeric elements (integers and floats) in a list.

    :param arr: The list to count numeric elements in.
    :return: The count of numeric elements in the list.
    """
    count = 0
    for item in arr:
        if isinstance(item, (int, float)):
            count += 1
    return count
