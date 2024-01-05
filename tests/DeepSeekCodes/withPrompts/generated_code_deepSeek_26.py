from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(remove_duplicates): 
    assert remove_duplicates([]) == [] 
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4] 
    assert remove_duplicates([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5] 
    
check(remove_duplicates)
