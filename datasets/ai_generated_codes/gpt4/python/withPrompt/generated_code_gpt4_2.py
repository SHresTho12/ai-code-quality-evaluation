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
