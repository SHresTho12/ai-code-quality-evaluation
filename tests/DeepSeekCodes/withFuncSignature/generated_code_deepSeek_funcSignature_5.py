# This is a generated Python file.
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return [element for pair in zip(numbers, [delimiter]*len(numbers)) for element in pair]


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(intersperse): 
    assert intersperse([], 7) == [] 
    assert intersperse([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2] 
    assert intersperse([2, 2, 2], 2) == [2, 2, 2, 2, 2] 
    
check(intersperse)