def is_bored(S, threshold=3):
    """
    Check if the string S contains any character that repeats consecutively
    more than 'threshold' times, which indicates boredom.
    """
    # Initialize a count and the previous character
    count = 1
    prev_char = None

    # Iterate through the string
    for char in S:
        # Check if the current character is the same as the previous one
        if char == prev_char:
            count += 1
            # If the count exceeds the threshold, return True (bored)
            if count > threshold:
                return True
        else:
            # Reset count and update previous character
            count = 1
            prev_char = char

    # If no character repeats more than the threshold, return False (not bored)
    return False

# Example usage
print(is_bored("I am soooo bored"))  # Output: True
print(is_bored("This is fun!"))      # Output: False
