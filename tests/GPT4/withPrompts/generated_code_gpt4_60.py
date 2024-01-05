def sum_to_n(n: int):
    """
    Return the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the range for summing.

    Returns:
    int: The sum of numbers from 1 to n.

    Examples:
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return (n * (n + 1)) // 2

# Example tests
print(sum_to_n(30))   # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
METADATA = {}

def check(sum_to_n):
    assert sum_to_n(1) == 1
    assert sum_to_n(6) == 21
    assert sum_to_n(11) == 66
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050

check(sum_to_n)