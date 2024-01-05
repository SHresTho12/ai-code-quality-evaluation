def get_row(lst, x):
    """
    Retrieves a row from a 2D list based on the given index.

    :param lst: A 2D list from which to retrieve the row.
    :param x: The index of the row to be retrieved.
    :return: The row from the 2D list at the specified index.
    """
    if 0 <= x < len(lst):
        return lst[x]
    else:
        raise IndexError("Index out of bounds")
