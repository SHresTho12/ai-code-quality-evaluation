from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    if not numbers:
        return []
    else:
        max_numbers = [numbers[0]]
        for num in numbers[1:]:
            max_numbers.append(max(max_numbers[-1], num))
        return max_numbers
    

METADATA = { 'author': 'jt', 'dataset': 'test' } 

def check(rolling_max): 
    assert rolling_max([]) == [] 
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4] 
    assert rolling_max([4, 3, 2, 1]) == [4, 4, 4, 4] 
    assert rolling_max([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100] 
    
check(rolling_max)