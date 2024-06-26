def is_prime(n: int) -> bool:
    """ Return True if n is a prime number, otherwise return False. """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

# Example usage
print(is_prime(11))  # True
print(is_prime(4))   # False
