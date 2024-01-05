def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    """Return the first n Fibonacci numbers that are also prime."""
    prime_fibs = []
    a, b = 0, 1
    while len(prime_fibs) < n:
        if is_prime(a):
            prime_fibs.append(a)
        a, b = b, a + b
    return prime_fibs

# Example usage
print(prime_fib(5))  # Example output: [2, 3, 5, 13, 89]
