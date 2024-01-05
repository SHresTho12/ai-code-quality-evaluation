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


def check(prime_length):
    # Check some simple cases
    assert prime_length('Hello') == True, "Test 1"
    assert prime_length('abcdcba') == True, "Test 2"
    assert prime_length('kittens') == True, "Test 3"
    assert prime_length('orange') == False, "Test 4"
    assert prime_length('wow') == True, "Test 5"
    assert prime_length('world') == True, "Test 6"
    assert prime_length('MadaM') == True, "Test 7"
    assert prime_length('Wow') == True, "Test 8"
    assert prime_length('') == False, "Test 9"
    assert prime_length('HI') == True, "Test 10"
    assert prime_length('go') == True, "Test 11"
    assert prime_length('gogo') == False, "Test 12"
    assert prime_length('aaaaaaaaaaaaaaa') == False, "Test 13"

check(prime_length)
