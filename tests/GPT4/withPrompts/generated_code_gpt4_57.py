def monotonic(l: list):
    """
    Check if the elements in the list are monotonically increasing or decreasing.

    Args:
    l (list): A list of elements.

    Returns:
    bool: True if the elements are monotonically increasing or decreasing, False otherwise.

    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    increasing = decreasing = True  # Initialize both flags to True

    for i in range(1, len(l)):
        if l[i] < l[i - 1]:
            increasing = False  # If any element is smaller than the previous, it's not increasing
        if l[i] > l[i - 1]:
            decreasing = False  # If any element is larger than the previous, it's not decreasing

    return increasing or decreasing  # Return True if either flag is True

# Example tests
print(monotonic([1, 2, 4, 20]))   # Output: True
print(monotonic([1, 20, 4, 10]))  # Output: False
print(monotonic([4, 1, 0, -10]))  # Output: True
METADATA = {}

def check(monotonic):
    assert monotonic([1, 2, 4, 10]) == True
    assert monotonic([1, 2, 4, 20]) == True
    assert monotonic([1, 20, 4, 10]) == False
    assert monotonic([4, 1, 0, -10]) == True
    assert monotonic([4, 1, 1, 0]) == True
    assert monotonic([1, 2, 3, 2, 5, 60]) == False
    assert monotonic([1, 2, 3, 4, 5, 60]) == True
    assert monotonic([9, 9, 9, 9]) == True

check(monotonic)
