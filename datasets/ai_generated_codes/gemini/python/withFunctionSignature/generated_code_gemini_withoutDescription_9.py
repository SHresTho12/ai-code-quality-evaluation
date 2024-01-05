
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculates the rolling maximum of a list of numbers, where each element
    in the output list is the maximum value seen so far in the input list up to that point.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers, where each element is the maximum value seen up to that index in the input list.
    """

    rolling_maxes = []
    current_max = float("-inf")  # Initialize with negative infinity to capture any initial value

    for number in numbers:
        current_max = max(current_max, number)  # Update current_max with the larger value
        rolling_maxes.append(current_max)  # Append the current maximum to the result list

    return rolling_maxes
