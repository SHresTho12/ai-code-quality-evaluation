from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """Remove all elements from a list of integers that occur more than once, maintaining the order.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with duplicates removed.

    Examples:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    return [num for num in numbers if counts[num] == 1]
