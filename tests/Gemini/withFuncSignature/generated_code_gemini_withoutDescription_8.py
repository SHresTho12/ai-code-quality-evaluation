
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of numbers, returning them as a tuple.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing two integers: the sum of the numbers and their product.
    """

    sum_of_numbers = sum(numbers)
    product_of_numbers = 1  # Initialize product as 1 to avoid multiplying by 0
    for number in numbers:
        product_of_numbers *= number

    return sum_of_numbers, product_of_numbers

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(sum_product): 
    assert sum_product([]) == (0, 1) 
    assert sum_product([1, 1, 1]) == (3, 1) 
    assert sum_product([100, 0]) == (100, 0) 
    assert sum_product([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7) 
    assert sum_product([10]) == (10, 10) 
    
check(sum_product)