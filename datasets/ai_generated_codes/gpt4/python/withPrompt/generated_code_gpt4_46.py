def fib4(n):
    """
    Calculate the n-th element of the Fib4 number sequence iteratively.

    Args:
    n (int): The index of the element to calculate.

    Returns:
    int: The n-th element of the Fib4 number sequence.

    Example:
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib_list = [0, 0, 2, 0]

    for i in range(4, n + 1):
        next_fib = sum(fib_list)
        fib_list.pop(0)
        fib_list.append(next_fib)

    return fib_list[-1]

# Example tests
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
