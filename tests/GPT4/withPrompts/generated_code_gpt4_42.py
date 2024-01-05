def incr_list(l: list) -> list:
    """
    Return a list with elements incremented by 1.

    Args:
    l (list): The input list of integers.

    Returns:
    list: A new list with elements incremented by 1.

    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Example tests
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
METADATA = {} 
def check(incr_list): 
    assert incr_list([]) == [] 
    assert incr_list([3, 2, 1]) == [4, 3, 2] 
    assert incr_list([5, 2, 5, 2, 3, 3, 9, 0, 123]) == [6, 3, 6, 3, 4, 4, 10, 1, 124] 
    
check(incr_list)