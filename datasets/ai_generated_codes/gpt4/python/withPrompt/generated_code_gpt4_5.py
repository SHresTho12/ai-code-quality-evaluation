from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """Insert a delimiter between every two consecutive elements of the input list.

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The delimiter to be inserted.

    Returns:
    List[int]: The modified list with the delimiter interspersed.

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    # Start with the first element
    result = [numbers[0]]

    # Iterate over the remaining elements, inserting the delimiter before each
    for number in numbers[1:]:
        result.extend([delimiter, number])

    return result
