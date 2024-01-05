def get_row(lst, x):
    """
    Find integers x in the list lst and return their coordinates as tuples.
    Sort coordinates initially by rows in ascending order and then by columns in descending order.
    """
    coordinates = []

    # Iterate through each row and column
    for row_index, row in enumerate(lst):
        for col_index, value in enumerate(row):
            if value == x:
                coordinates.append((row_index, col_index))

    # Sort coordinates by rows in ascending order and by columns in descending order
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))

    return coordinates
