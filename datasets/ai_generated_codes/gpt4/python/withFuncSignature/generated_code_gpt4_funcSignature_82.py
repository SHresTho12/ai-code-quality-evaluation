def is_prime(n):
    """Check if a number is prime."""
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

def prime_length(string):
    """
    Determines if the length of a string is a prime number.

    :param string: The input string.
    :return: True if the length of the string is a prime number, False otherwise.
    """
    return is_prime(len(string))
