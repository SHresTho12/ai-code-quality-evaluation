def sort_even(l: list) -> list:
    """Sort elements at even indices in a list, keeping the elements at odd indices in their original positions.

    Args:
    l (list): The input list.

    Returns:
    list: The modified list with specified elements sorted.

    Examples:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices_values = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indices_values.sort()

    result = []
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_indices_values[even_index])
            even_index += 1
        else:
            result.append(l[i])

    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
METADATA = {} 
def check(sort_even): 
    assert tuple(sort_even([1, 2, 3])) == tuple([1, 2, 3]) 
    assert tuple(sort_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123]) 
    assert tuple(sort_even([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10]) 
    
check(sort_even)