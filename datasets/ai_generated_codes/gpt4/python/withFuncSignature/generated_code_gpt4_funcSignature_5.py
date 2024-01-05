from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    interspersed = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:
        interspersed.extend([delimeter, num])  # Add delimeter and the next number

    return interspersed
