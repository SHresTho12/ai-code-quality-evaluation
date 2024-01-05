def below_threshold(l: list, t: int):
    """
    Check if all numbers in a list are below a threshold.

    Args:
    l (list): The input list of numbers.
    t (int): The threshold to check against.

    Returns:
    bool: True if all numbers are below the threshold, False otherwise.

    Example:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < t for num in l)

# Example tests
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))  # Output: False
