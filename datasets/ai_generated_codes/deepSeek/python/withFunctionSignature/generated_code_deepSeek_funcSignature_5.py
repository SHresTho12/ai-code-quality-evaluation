# This is a generated Python file.
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return [element for pair in zip(numbers, [delimiter]*len(numbers)) for element in pair]