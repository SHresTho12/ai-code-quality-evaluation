def any_int(x, y, z):
    """
    Returns True if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns False in any other cases.
    """
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x == y + z or y == x + z or z == x + y:
            return True
    return False

# Test cases
print(any_int(5, 2, 7))      # Output: True
print(any_int(3, 2, 2))      # Output: False
print(any_int(3, -2, 1))     # Output: True
print(any_int(3.6, -2.2, 2)) # Output: False
