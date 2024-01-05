
def digitSum(s):
    # Initialize the sum to 0
    total = 0

    # Iterate through each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # Add its integer value to the total
            total += int(char)

    return total

# Example usage
print(digitSum("abc123"))  # Output: 6
print(digitSum("12345"))   # Output: 15
print(digitSum("a1b2c3"))  # Output: 6
