def rounded_avg(n, m):
    # Check if n is greater than m, return -1 in that case
    if n > m:
        return -1

    # Calculate the sum of integers from n through m
    total_sum = sum(range(n, m + 1))
    
    # Calculate the average
    avg = total_sum / (m - n + 1)
    
    # Round the average to the nearest integer
    rounded_avg = round(avg)
    
    # Convert the rounded average to binary format
    binary_avg = bin(rounded_avg)
    
    return binary_avg

# Test cases
print(rounded_avg(1, 5))    # Output: "0b11"
print(rounded_avg(7, 5))    # Output: -1
print(rounded_avg(10, 20))  # Output: "0b1111"
print(rounded_avg(20, 33))  # Output: "0b11010"
