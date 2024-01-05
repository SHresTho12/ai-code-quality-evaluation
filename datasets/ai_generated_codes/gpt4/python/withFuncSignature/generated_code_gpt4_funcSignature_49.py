def modp(n: int, p: int, M=int(1e9+7)):
    # Initialize the result
    result = 1

    # Update n to be n modulo M
    n = n % M

    while p > 0:
        # If p is odd, multiply n with result
        if p % 2 == 1:
            result = (result * n) % M

        # Now p must be even, divide it by 2
        p = p // 2
        n = (n * n) % M

    return result

# Example usage
print(modp(2, 10))  # Output: 1024
print(modp(2, 100))  # Output: a large number modulo 10^9 + 7
