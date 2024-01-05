
def truncate_number(number: float) -> float:
    """
    Truncates a floating-point number to its whole number part, removing any decimal portion.

    Args:
        number: The floating-point number to truncate.

    Returns:
        The truncated number as a float.
    """

    return int(number)  # Cast the number to an integer to remove decimals

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(truncate_number): 
    assert truncate_number(3.5) == 0.5 
    assert abs(truncate_number(1.33) - 0.33) < 1e-6 
    assert abs(truncate_number(123.456) - 0.456) < 1e-6 
    
check(truncate_number)
