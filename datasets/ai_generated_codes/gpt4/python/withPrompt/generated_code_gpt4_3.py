from typing import List

def below_zero(operations: List[int]) -> bool:
    """Check if the balance of an account falls below zero after a series of operations.

    Args:
    operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
    bool: True if the balance falls below zero at any point, otherwise False.

    Examples:
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
