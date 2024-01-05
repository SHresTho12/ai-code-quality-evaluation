def truncate_number(number: float) -> float:
    """Return the decimal part of a given positive floating point number.

    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(truncate_number): 
    assert truncate_number(3.5) == 0.5 
    assert abs(truncate_number(1.33) - 0.33) < 1e-6 
    assert abs(truncate_number(123.456) - 0.456) < 1e-6 
    
check(truncate_number)
