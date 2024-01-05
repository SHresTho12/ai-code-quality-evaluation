from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Calculate the sum and product of all integers in a list.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple consisting of the sum and product of the integers.

    Examples:
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_of_numbers = sum(numbers)
    product_of_numbers = 1

    for number in numbers:
        product_of_numbers *= number

    return sum_of_numbers, product_of_numbers
