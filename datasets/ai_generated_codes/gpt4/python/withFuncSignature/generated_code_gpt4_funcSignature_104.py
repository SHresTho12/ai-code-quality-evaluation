def unique_digits(x):
    """
    Counts the number of unique digits in an integer.

    :param x: The integer to count unique digits in.
    :return: The count of unique digits.
    """
    # Convert the integer to a string to iterate through its characters
    x_str = str(x)

    # Use a set to store unique digits
    unique_digit_set = set()

    # Iterate through the characters and add unique digits to the set
    for char in x_str:
        if char.isdigit():
            unique_digit_set.add(char)

    # Return the count of unique digits
    return len(unique_digit_set)
