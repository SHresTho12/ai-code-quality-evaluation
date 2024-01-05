def sum_to_n(n: int):
    """
    Calculates the sum of all positive integers up to and including 'n'.

    :param n: The maximum integer to sum up to.
    :return: The sum of all integers from 1 to 'n'.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer")

    return n * (n + 1) // 2
