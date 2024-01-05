def odd_count(lst):
    """
    Counts the number of odd integers in a list.

    :param lst: The list to count odd integers in.
    :return: The count of odd integers in the list.
    """
    count = 0
    for num in lst:
        if num % 2 == 1:
            count += 1
    return count
