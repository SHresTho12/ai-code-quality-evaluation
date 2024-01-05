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

METADATA = {}

def check(below_threshold):
    assert below_threshold([1, 2, 4, 10], 100)
    assert not below_threshold([1, 20, 4, 10], 5)
    assert below_threshold([1, 20, 4, 10], 21)
    assert below_threshold([1, 20, 4, 10], 22)
    assert below_threshold([1, 8, 4, 10], 11)
    assert not below_threshold([1, 8, 4, 10], 10)

check(below_threshold)