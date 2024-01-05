def is_palindrome(text):
    """
    Check if given string is a palindrome.

    Args:
    text (str): The input string.

    Returns:
    bool: True if the string is a palindrome, False otherwise.

    Example:
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove spaces and convert to lowercase (if case-insensitive comparison is needed)
    text = text.replace(" ", "").lower()
    # Compare the string with its reverse
    return text == text[::-1]

# Example tests
print(is_palindrome(''))       # Output: True
print(is_palindrome('aba'))    # Output: True
print(is_palindrome('aaaaa'))  # Output: True
print(is_palindrome('zbcd'))   # Output: False
