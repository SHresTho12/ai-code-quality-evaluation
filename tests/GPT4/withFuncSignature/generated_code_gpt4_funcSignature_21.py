from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []

    min_num = min(numbers)
    max_num = max(numbers)

    # Handle the case where all numbers are the same
    if min_num == max_num:
        return [1.0 for _ in numbers]

    range_num = max_num - min_num
    return [(num - min_num) / range_num for num in numbers]

# Example usage
test_numbers = [10, 15, 20, 25, 30]
result = rescale_to_unit(test_numbers)
result
METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(rescale_to_unit): 
    assert rescale_to_unit([2.0, 49.9]) == [0.0, 1.0] 
    assert rescale_to_unit([100.0, 49.9]) == [1.0, 0.0] 
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0] 
    assert rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75] 
    assert rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75] 
    
check(rescale_to_unit)