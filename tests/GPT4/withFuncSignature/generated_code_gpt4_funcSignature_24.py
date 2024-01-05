import math


def largest_divisor(n: int) -> int:
    """ Return the largest divisor of n, other than n itself. """
    if n <= 1:
        raise ValueError("Input must be greater than 1.")

    # Start checking from the largest possible divisor, which is less than n
    for i in range(int(math.sqrt(n)), 0, -1):
        if n % i == 0:
            # Return the corresponding larger divisor
            return n // i

    # If no divisor is found (which shouldn't happen), return 1
    return 1

# Example usage
result = largest_divisor(100)  # Should return 50
result
METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(largest_divisor): 
    assert largest_divisor(3) == 1 
    assert largest_divisor(7) == 1 
    assert largest_divisor(10) == 5 
    assert largest_divisor(100) == 50 
    assert largest_divisor(49) == 7 
    
check(largest_divisor)