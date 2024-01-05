from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """Generate a list of rolling maximum elements from a given list of integers.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list where each element is the maximum of all elements seen so far in the sequence.

    Examples:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_so_far = numbers[0]
    rolling_maxes = [max_so_far]

    for number in numbers[1:]:
        max_so_far = max(max_so_far, number)
        rolling_maxes.append(max_so_far)

    return rolling_maxes
