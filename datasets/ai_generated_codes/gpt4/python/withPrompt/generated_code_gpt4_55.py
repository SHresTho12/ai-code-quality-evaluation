def fib(n: int):
    """
    Return n-th Fibonacci number.

    Args:
    n (int): The index of the Fibonacci number to calculate.

    Returns:
    int: The n-th Fibonacci number.

    Examples:
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Example tests
print(fib(10))  # Output: 55
print(fib(1))   # Output: 1
print(fib(8))   # Output: 21
