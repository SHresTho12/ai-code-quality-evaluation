def solve(N):
    # Convert the number to binary
    binary = bin(N)[2:]
    # Calculate the sum of digits
    total = sum(int(digit) for digit in binary)
    # Return the sum in binary
    return bin(total)[2:]