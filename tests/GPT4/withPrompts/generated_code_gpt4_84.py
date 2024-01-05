def solve(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.
    """
    # Convert the integer N to a string to easily extract its digits.
    N_str = str(N)
    
    # Calculate the sum of digits.
    digit_sum = sum(int(digit) for digit in N_str)
    
    # Convert the digit sum to binary and remove the "0b" prefix.
    binary_sum = bin(digit_sum)[2:]
    
    return binary_sum
def check(solve):
    # Check some simple cases
    assert solve(1000) == "1", "Test 1"
    assert solve(150) == "110", "Test 2"
    assert solve(147) == "1100", "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert solve(333) == "1001", "Test 4"
    assert solve(963) == "10010", "Test 5"

check(solve)
