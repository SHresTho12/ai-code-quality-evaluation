def next_smallest(lst):
    """
    Replaces each element in the list with the next smallest element in the list.
    If there is no smaller element, the value is replaced with -1.

    :param lst: A list of integers.
    :return: A new list with each element replaced by the next smallest element.
    """
    result = []
    for i in range(len(lst)):
        next_smaller = -1  # Default value if no smaller element is found
        for j in range(len(lst)):
            if lst[j] < lst[i]:
                # Check if this is the first smaller element found or if it's smaller than the current next_smaller
                if next_smaller == -1 or lst[j] > next_smaller:
                    next_smaller = lst[j]
        result.append(next_smaller)
    return result


def check(next_smallest):
    # Check some simple cases
    assert next_smallest([1, 2, 3, 4, 5]) == 2, "Error"
    assert next_smallest([5, 1, 4, 3, 2]) == 2, "Error"
    assert next_smallest([]) == None, "Error"
    assert next_smallest([1, 1]) == None, "Error"
    assert next_smallest([1, 1, 1, 1, 0]) == 1, "Error"
    assert next_smallest([1, 0**0]) == None, "Error"
    assert next_smallest([-35, 34, 12, -45]) == -35, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

check(next_smallest)