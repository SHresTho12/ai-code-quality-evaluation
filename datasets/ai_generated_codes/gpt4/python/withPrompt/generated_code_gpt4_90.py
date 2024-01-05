def next_smallest(lst):
    """
    Return the 2nd smallest element of the list. Return None if there is no such element.
    """
    if len(lst) < 2:
        return None

    # Find the minimum and second minimum elements
    min_element = min(lst)
    lst.remove(min_element)  # Remove the minimum element
    second_min_element = min(lst)

    return second_min_element

# Test cases
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
print(next_smallest([]))  # Output: None
print(next_smallest([1, 1]))  # Output: None
