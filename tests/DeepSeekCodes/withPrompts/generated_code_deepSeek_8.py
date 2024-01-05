import operator
from functools import reduce
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    else:
        sum_numbers = sum(numbers)
        product_numbers = reduce(operator.mul, numbers, 1)
        return (sum_numbers, product_numbers)
    

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(sum_product): 
    assert sum_product([]) == (0, 1) 
    assert sum_product([1, 1, 1]) == (3, 1) 
    assert sum_product([100, 0]) == (100, 0) 
    assert sum_product([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7) 
    assert sum_product([10]) == (10, 10) 
    
check(sum_product)