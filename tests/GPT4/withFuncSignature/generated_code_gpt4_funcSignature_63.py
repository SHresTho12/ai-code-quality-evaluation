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


METADATA = {}

def check(fibfib):
    assert fibfib(2) == 1
    assert fibfib(1) == 0
    assert fibfib(5) == 4
    assert fibfib(8) == 24
    assert fibfib(10) == 81
    assert fibfib(12) == 274
    assert fibfib(14) == 927

check(fibfib)