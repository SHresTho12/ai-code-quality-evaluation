
def greatest_common_divisor(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The greatest common divisor of a and b.
    """

    while b != 0:
        a, b = b, a % b  # Repeatedly swap a and b with the remainder until b becomes 0
    return a  # The GCD is the final value of a

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(greatest_common_divisor): 
    assert greatest_common_divisor(3, 7) == 1 
    assert greatest_common_divisor(10, 15) == 5 
    assert greatest_common_divisor(49, 14) == 7 
    assert greatest_common_divisor(144, 60) == 12 
    
check(greatest_common_divisor)