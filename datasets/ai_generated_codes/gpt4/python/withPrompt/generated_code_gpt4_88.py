def sort_array(array):
    """
    Sort the given array in ascending order if the sum of the first and last elements is odd,
    otherwise sort it in descending order.
    """
    if not array:
        return []

    first_value = array[0]
    last_value = array[-1]
    total = first_value + last_value

    if total % 2 == 1:
        # If the sum is odd, sort in ascending order
        return sorted(array)
    else:
        # If the sum is even, sort in descending order
        return sorted(array, reverse=True)
