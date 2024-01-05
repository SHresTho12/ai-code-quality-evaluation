from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    return [(num - min_val) / range_val for num in numbers]


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(rescale_to_unit): 
    assert rescale_to_unit([2.0, 49.9]) == [0.0, 1.0] 
    assert rescale_to_unit([100.0, 49.9]) == [1.0, 0.0] 
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0] 
    assert rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75] 
    assert rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75] 
    
check(rescale_to_unit)