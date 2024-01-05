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
