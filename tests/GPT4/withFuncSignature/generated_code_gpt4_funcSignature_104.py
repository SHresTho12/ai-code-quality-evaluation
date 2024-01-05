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


def check(unique_digits):
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33], "Test 1"
    assert unique_digits([152, 323, 1422, 10]) == [], "Test 2"
    assert unique_digits([12345, 2033, 111, 151]) == [111, 151], "Test 3"
    assert unique_digits([135, 103, 31]) == [31, 135], "Test 4"

# Check some edge cases that are easy to work out by hand.
assert True, "This prints if this assert fails (also good for debugging!)"

check(unique_digits)