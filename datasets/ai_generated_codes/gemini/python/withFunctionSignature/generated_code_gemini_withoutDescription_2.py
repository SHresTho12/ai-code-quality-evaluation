
def truncate_number(number: float) -> float:
    """
    Truncates a floating-point number to its whole number part, removing any decimal portion.

    Args:
        number: The floating-point number to truncate.

    Returns:
        The truncated number as a float.
    """

    return int(number)  # Cast the number to an integer to remove decimals
