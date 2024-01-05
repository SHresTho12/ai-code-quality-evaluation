def fib4(n: int):
    # Handle the base cases
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2

    # Initialize the first four numbers of the sequence
    a, b, c, d = 0, 1, 1, 2

    # Calculate the nth number
    for i in range(4, n):
        a, b, c, d = b, c, d, a + b + c + d

    return d

# Example usage
print(fib4(5))  # Output: 4 (since the sequence would be 0, 1, 1, 2, 4)
