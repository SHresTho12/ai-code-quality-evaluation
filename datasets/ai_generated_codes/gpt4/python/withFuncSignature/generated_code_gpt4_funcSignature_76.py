def is_simple_power(x, n):
    # Check for invalid cases
    if x <= 0 or n <= 1:
        return False

    # Keep dividing x by n while it is divisible
    while x % n == 0:
        x = x // n

    # If x becomes 1, it is a simple power of n
    return x == 1

# Example usage
print(is_simple_power(8, 2))    # Output: True (since 8 = 2^3)
print(is_simple_power(27, 3))   # Output: True (since 27 = 3^3)
print(is_simple_power(20, 2))   # Output: False (since 20 is not a power of 2)
