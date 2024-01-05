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
