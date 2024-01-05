def sum_to_n(n: int):
    """
    Calculates the sum of all positive integers up to and including 'n'.

    :param n: The maximum integer to sum up to.
    :return: The sum of all integers from 1 to 'n'.
    """
    if n < 0:
        raise ValueError("Input should be a non-negative integer")

    return n * (n + 1) // 2


METADATA = {}

def check(sum_to_n):
    assert sum_to_n(1) == 1
    assert sum_to_n(6) == 21
    assert sum_to_n(11) == 66
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050

check(sum_to_n)