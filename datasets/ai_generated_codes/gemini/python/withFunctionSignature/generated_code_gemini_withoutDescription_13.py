
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
