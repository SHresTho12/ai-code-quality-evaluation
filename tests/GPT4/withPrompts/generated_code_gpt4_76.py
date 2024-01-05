def is_simple_power(x, n):
    """
    Return True if a number x is a simple power of n, False otherwise.
    x is a simple power of n if n^int(x) == x.

    Args:
    x (int): The input number.
    n (int): The base number.

    Returns:
    bool: True if x is a simple power of n, False otherwise.

    Example:
    >>> is_simple_power(1, 4)
    True
    >>> is_simple_power(2, 2)
    True
    >>> is_simple_power(8, 2)
    True
    >>> is_simple_power(3, 2)
    False
    >>> is_simple_power(3, 1)
    False
    >>> is_simple_power(5, 3)
    False
    """
    
    # Check if x is 1, as any number to the power of 0 is 1
    if x == 1:
        return True

    # Check if n is 1, as 1 to any power is still 1
    if n == 1:
        return False

    # Initialize a variable to keep track of the current power
    power = 1

    # Keep multiplying n by itself until it's greater than or equal to x
    while n ** power < x:
        power += 1

    # Check if n raised to the calculated power is equal to x
    return n ** power == x

def check(is_simple_power):
    # Check some simple cases
    assert is_simple_power(1, 4) == True, "Test 1"
    assert is_simple_power(2, 2) == True, "Test 2"
    assert is_simple_power(8, 2) == True, "Test 3"
    assert is_simple_power(3, 2) == False, "Test 4"
    assert is_simple_power(3, 1) == False, "Test 5"
    assert is_simple_power(5, 3) == False, "Test 6"
    
    # Check some additional simple cases
    assert is_simple_power(16, 2) == True, "Test 7"
    assert is_simple_power(143214, 16) == False, "Test 8"
    assert is_simple_power(4, 2) == True, "Test 9"
    assert is_simple_power(9, 3) == True, "Test 10"
    assert is_simple_power(16, 4) == True, "Test 11"
    assert is_simple_power(24, 2) == False, "Test 12"
    assert is_simple_power(128, 4) == False, "Test 13"
    assert is_simple_power(12, 6) == False, "Test 14"
    
    # Check some edge cases that are easy to work out by hand.
    assert is_simple_power(1, 1) == True, "Test 15"
    assert is_simple_power(1, 12) == True, "Test 16"

check(is_simple_power)