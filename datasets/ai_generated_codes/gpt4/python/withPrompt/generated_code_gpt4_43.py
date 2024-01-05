def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.

    Args:
    l (list): The input list of integers.

    Returns:
    bool: True if there are two distinct elements that sum to zero, False otherwise.

    Examples:
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # Create a set to store seen elements
    seen = set()
    
    for num in l:
        # Check if the negative of the current number is in the set
        if -num in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    
    return False

# Example tests
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(pairs_sum_to_zero([1]))  # Output: False
