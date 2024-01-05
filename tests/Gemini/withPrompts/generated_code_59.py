
def largest_prime_factor(n: int) -> int:
    """Efficiently finds the largest prime factor of n."""

    largest_factor = 1  # Initialize to track the largest prime factor

    # Iterate up to the square root of n to efficiently find factors
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:  # Repeatedly divide by i as long as it's a factor
            largest_factor = i  # Update largest prime factor found
            n //= i

    # If n is still greater than 1, it means it has a prime factor greater than its square root
    return largest_factor if n == 1 else n


METADATA = {}

def check(largest_prime_factor):
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(63) == 7
    assert largest_prime_factor(330) == 11
    assert largest_prime_factor(13195) == 29

check(largest_prime_factor)
