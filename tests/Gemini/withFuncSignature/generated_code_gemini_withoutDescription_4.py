
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculates the mean absolute deviation (MAD) of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The mean absolute deviation of the numbers.
    """

    if not numbers:
        return 0  # Handle empty list

    mean = sum(numbers) / len(numbers)
    deviations = [abs(number - mean) for number in numbers]
    return sum(deviations) / len(numbers)

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(mean_absolute_deviation): 
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6 
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6 
    assert abs(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6 

check(mean_absolute_deviation)