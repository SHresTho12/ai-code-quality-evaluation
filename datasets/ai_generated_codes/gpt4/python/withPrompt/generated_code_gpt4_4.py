from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate the Mean Absolute Deviation (MAD) of a list of numbers.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the numbers.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the sum of absolute differences from the mean
    total_deviation = sum(abs(x - mean) for x in numbers)

    # Calculate the mean absolute deviation
    mad = total_deviation / len(numbers)
    return mad
