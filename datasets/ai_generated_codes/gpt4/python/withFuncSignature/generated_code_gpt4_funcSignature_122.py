def add_elements(arr, k):
    """
    Adds a value 'k' to each element in a list.

    :param arr: The input list.
    :param k: The value to add to each element.
    :return: A new list containing elements with 'k' added to each.
    """
    # Use a list comprehension to add 'k' to each element
    result = [x + k for x in arr]
    return result
