# This is a generated Python file.
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    closest_pair = (numbers[0], numbers[1])
    min_difference = closest_pair[1] - closest_pair[0]
    for i in range(1, len(numbers) - 1):
        pair = (numbers[i], numbers[i + 1])
        difference = pair[1] - pair[0]
        if difference < min_difference:
            closest_pair = pair
            min_difference = difference
    return closest_pair


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(find_closest_elements): 
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0) 
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9) 
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2) 
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0) 
    assert find_closest_elements([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1) 
    
check(find_closest_elements)
