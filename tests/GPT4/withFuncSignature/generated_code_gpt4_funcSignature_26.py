from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if not (x in seen or seen.add(x))]

# Example usage
test_numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
result = remove_duplicates(test_numbers)
result


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(remove_duplicates): 
    assert remove_duplicates([]) == [] 
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4] 
    assert remove_duplicates([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5] 
    
check(remove_duplicates)
