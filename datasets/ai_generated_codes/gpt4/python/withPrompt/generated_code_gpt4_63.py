def fibfib(n: int):
    """
    Compute the n-th element of the FibFib number sequence.

    Args:
    n (int): The index of the desired element in the sequence.

    Returns:
    int: The n-th element of the FibFib sequence.

    Examples:
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_values = [0, 0, 1]
        for i in range(3, n + 1):
            next_value = fibfib_values[-1] + fibfib_values[-2] + fibfib_values[-3]
            fibfib_values.append(next_value)
        return fibfib_values[-1]

# Example tests
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
