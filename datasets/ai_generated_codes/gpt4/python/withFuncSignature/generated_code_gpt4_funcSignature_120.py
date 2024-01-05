def maximum(arr, k):
    """
    Finds the k maximum elements from a list in descending order.

    :param arr: The input list.
    :param k: The number of maximum elements to find.
    :return: A list containing the k maximum elements.
    """
    # Sort the input list in descending order
    arr.sort(reverse=True)

    # Slice the list to select the first k elements
    max_elements = arr[:k]

    return max_elements
