from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    interspersed = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:
        interspersed.extend([delimeter, num])  # Add delimeter and the next number

    return interspersed
METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(intersperse): 
    assert intersperse([], 7) == [] 
    assert intersperse([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2] 
    assert intersperse([2, 2, 2], 2) == [2, 2, 2, 2, 2] 
    
check(intersperse)