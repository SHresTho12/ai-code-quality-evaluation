from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Apply a linear transformation to a list of numbers so the smallest becomes 0 and the largest becomes 1.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    List[float]: The transformed list of numbers.

    Examples:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")

    min_num = min(numbers)
    max_num = max(numbers)

    if min_num == max_num:
        raise ValueError("List elements must not be all identical.")

    range_num = max_num - min_num
    return [(num - min_num) / range_num for num in numbers]
