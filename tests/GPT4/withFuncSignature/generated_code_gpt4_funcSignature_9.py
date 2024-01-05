
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []

    max_so_far = numbers[0]
    result = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)

    return result
METADATA = { 'author': 'jt', 'dataset': 'test' } 

def check(rolling_max): 
    assert rolling_max([]) == [] 
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4] 
    assert rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4] 
    assert rolling_max([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100] 
    
check(rolling_max)