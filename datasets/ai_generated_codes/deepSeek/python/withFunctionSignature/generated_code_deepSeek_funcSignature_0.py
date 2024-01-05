# This is a generated Python file.
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) <= threshold for a in numbers for b in numbers if a != b)