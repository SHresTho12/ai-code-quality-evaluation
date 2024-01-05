def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Check if a number is a product of two prime numbers."""
    if a < 4:  # The smallest product of two primes is 2*2=4
        return False

    for i in range(2, int(a**0.5) + 1):
        if a % i == 0 and is_prime(i) and is_prime(a // i):
            return True

    return False

# Example usage
print(is_multiply_prime(15))  # Output: True (since 15 = 3 * 5, both primes)
print(is_multiply_prime(20))  # Output: False (since 20 = 2 * 2 * 5, where 2*2 is not a prime)
