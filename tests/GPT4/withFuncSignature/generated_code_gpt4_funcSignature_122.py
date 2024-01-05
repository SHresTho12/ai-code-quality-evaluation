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


def check(add_elements):
    # Check some simple cases
    assert add_elements([1, -2, -3, 41, 57, 76, 87, 88, 99], 3) == -4, "Test 1"
    assert add_elements([111, 121, 3, 4000, 5, 6], 2) == 0, "Test 2"
    assert add_elements([11, 21, 3, 90, 5, 6, 7, 8, 9], 4) == 125, "Test 3"
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24, "Test 4"

    # Check the function
    check(add_elements)
