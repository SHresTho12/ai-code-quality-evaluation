def choose_num(x, y):
    # Initialize a variable to store the largest even integer
    largest_even = -1
    
    # Iterate through the range from x to y inclusive
    for num in range(x, y + 1):
        # Check if the number is even
        if num % 2 == 0:
            # Update the largest_even if the current number is larger
            if num > largest_even:
                largest_even = num
    
    return largest_even

# Test cases
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1

def check(choose_num):
    assert choose_num(12, 15) == 14, "Test 1"
    assert choose_num(13, 12) == -1, "Test 2"
    assert choose_num(33, 12354) == 12354, "Test 3"
    assert choose_num(5234, 5233) == -1, "Test 4"
    assert choose_num(6, 29) == 28, "Test 5"
    assert choose_num(27, 10) == -1, "Test 6"

# Check some edge cases that are easy to work out by hand.
assert choose_num(7, 7) == -1, "Edge Test 1"
assert choose_num(546, 546) == 546, "Edge Test 2"

check(choose_num)