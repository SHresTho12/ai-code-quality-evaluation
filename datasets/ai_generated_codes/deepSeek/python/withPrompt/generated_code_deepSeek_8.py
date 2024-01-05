from typing import List, Tuple
from functools import reduce
import operator

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    else:
        sum_numbers = sum(numbers)
        product_numbers = reduce(operator.mul, numbers, 1)
        return (sum_numbers, product_numbers)