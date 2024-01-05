from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """Find and return the two closest elements in the list, in ascending order.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    Tuple[float, float]: A tuple of the two closest numbers, in ascending order.

    Examples:
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers.")

    # Sort the list to make comparison easier
    sorted_numbers = sorted(numbers)

    # Initialize variables to store the closest pair and minimum difference found
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    min_diff = abs(sorted_numbers[1] - sorted_numbers[0])

    # Iterate over the list and check each pair
    for i in range(1, len(sorted_numbers) - 1):
        current_diff = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if current_diff < min_diff:
            min_diff = current_diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])

    return closest_pair
