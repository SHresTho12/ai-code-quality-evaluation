def is_simple_power(x, n):
    # Check for invalid cases
    if x <= 0 or n <= 1:
        return False

    # Keep dividing x by n while it is divisible
    while x % n == 0:
        x = x // n

    # If x becomes 1, it is a simple power of n
    return x == 1

# Example usage
print(is_simple_power(8, 2))    # Output: True (since 8 = 2^3)
print(is_simple_power(27, 3))   # Output: True (since 27 = 3^3)
print(is_simple_power(20, 2))   # Output: False (since 20 is not a power of 2)


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