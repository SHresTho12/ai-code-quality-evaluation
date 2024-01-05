def largest_prime_factor(n: int):
    # Handle the case of n being less than 2
    if n < 2:
        return None

    # Divide n by 2 to remove all even factors
    largest_factor = 2
    while n % 2 == 0:
        n //= 2

    # Divide n by all odd factors starting from 3
    factor = 3
    while n > 1:
        if n % factor == 0:
            largest_factor = factor
            while n % factor == 0:
                n //= factor
        factor += 2

    return largest_factor

# Example usage
print(largest_prime_factor(28))  # Output: 7

METADATA = {}

def check(largest_prime_factor):
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(27) == 3
    assert largest_prime_factor(63) == 7
    assert largest_prime_factor(330) == 11
    assert largest_prime_factor(13195) == 29

check(largest_prime_factor)