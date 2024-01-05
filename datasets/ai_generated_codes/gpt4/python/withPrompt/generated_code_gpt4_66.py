def digitSum(s):
    """Calculate the sum of ASCII codes of uppercase characters in a string.

    Args:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of uppercase characters.

    Examples:
    >>> digitSum("")
    0
    >>> digitSum("abAB")
    131
    >>> digitSum("abcCd")
    67
    >>> digitSum("helloE")
    69
    >>> digitSum("woArBld")
    131
    >>> digitSum("aAaaaXa")
    153
    """
    # Initialize the sum to 0
    total_sum = 0

    # Iterate through each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII code of the uppercase character to the total sum
            total_sum += ord(char)

    return total_sum
