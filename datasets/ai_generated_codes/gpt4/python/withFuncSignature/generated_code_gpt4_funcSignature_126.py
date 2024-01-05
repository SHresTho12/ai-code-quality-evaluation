def is_sorted(lst):
    """
    Checks if a list is sorted in ascending order.

    :param lst: The input list to be checked.
    :return: True if the list is sorted, False otherwise.
    """
    # Iterate through the list and compare adjacent elements
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False  # If any pair of adjacent elements is out of order, return False
    
    return True  # If the loop completes without finding any out-of-order pair, return True
