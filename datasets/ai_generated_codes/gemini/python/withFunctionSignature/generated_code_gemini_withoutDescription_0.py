
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks if there are any two numbers in the list that are closer to each other than the given threshold.

    Args:
        numbers: A list of numbers to check.
        threshold: The maximum distance allowed between two numbers to be considered "close".

    Returns:
        True if there are any two close numbers in the list, False otherwise.
    """

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # Start from i+1 to avoid redundant comparisons
            if abs(numbers[i] - numbers[j]) < threshold:
                return True

    return False
