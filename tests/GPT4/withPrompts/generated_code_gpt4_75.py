def is_multiply_prime(a):
    """
    Return True if the given number is the multiplication of 3 prime numbers, False otherwise.

    Args:
    a (int): The input number (a) which is less than 100.

    Returns:
    bool: True if a is the multiplication of 3 prime numbers, False otherwise.

    Example:
    >>> is_multiply_prime(30)
    True
    """
    
    # Function to check if a number is prime
    def is_prime(n):
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

    # Check if a is less than 100
    if a >= 100:
        return False

    # Find the prime factors of a
    prime_factors = []
    i = 2
    while i * i <= a:
        if a % i:
            i += 1
        else:
            a //= i
            if is_prime(i):
                prime_factors.append(i)
    if a > 1:
        prime_factors.append(a)

    # Check if there are exactly 3 prime factors
    return len(prime_factors) == 3
def check(is_multiply_prime):
    assert is_multiply_prime(5) == False
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(8) == True
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(125) == True
    assert is_multiply_prime(3 * 5 * 7) == True
    assert is_multiply_prime(3 * 6 * 7) == False
    assert is_multiply_prime(9 * 9 * 9) == False
    assert is_multiply_prime(11 * 9 * 9) == False
    assert is_multiply_prime(11 * 13 * 7) == True

check(is_multiply_prime)
