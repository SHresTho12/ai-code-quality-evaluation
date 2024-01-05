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
