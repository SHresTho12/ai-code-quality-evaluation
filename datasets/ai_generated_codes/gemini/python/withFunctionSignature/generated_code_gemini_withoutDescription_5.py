
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Intersperses a delimiter between each element of a list of numbers.

    Args:
        numbers: A list of integers.
        delimiter: The integer to insert between each element.

    Returns:
        A new list with the delimiter inserted between each original element.
    """

    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:  # Avoid adding the delimiter after the last element
            result.append(delimiter)
    return result
