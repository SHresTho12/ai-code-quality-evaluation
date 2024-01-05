def fibfib(n: int):
    # Handle the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize the first two numbers of the sequence
    a, b = 0, 1

    # Calculate the nth number
    for _ in range(2, n + 1):
        a, b = b, a**2 + b**2

    return b

# Example usage
print(fibfib(5))  # Example output for the defined rule
