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
def check(rounded_avg):
    assert rounded_avg(1, 5) == "0b11", "Test 1"
    assert rounded_avg(7, 13) == "0b1010", "Test 2"
    assert rounded_avg(964, 977) == "0b1111001010", "Test 3"
    assert rounded_avg(996, 997) == "0b1111100100", "Test 4"
    assert rounded_avg(560, 851) == "0b1011000010", "Test 5"
    assert rounded_avg(185, 546) == "0b101101110", "Test 6"
    assert rounded_avg(362, 496) == "0b110101101", "Test 7"
    assert rounded_avg(350, 902) == "0b1001110010", "Test 8"
    assert rounded_avg(197, 233) == "0b11010111", "Test 9"

# Check some edge cases that are easy to work out by hand.
assert rounded_avg(7, 5) == -1, "Edge Test 1"
assert rounded_avg(5, 1) == -1, "Edge Test 2"
assert rounded_avg(5, 5) == "0b101", "Edge Test 3"

check(rounded_avg)

