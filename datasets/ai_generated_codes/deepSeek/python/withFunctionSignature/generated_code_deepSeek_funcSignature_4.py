# This is a generated Python file.
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(number - mean) for number in numbers) / len(numbers)