
def make_palindrome(string: str) -> str:
    """
    Creates a palindrome from the given string by appending characters to the end of it
    until it becomes a palindrome.

    Args:
        string: The input string to transform into a palindrome.

    Returns:
        The palindrome created by appending characters to the original string.
    """

    while not is_palindrome(string):
        string += string[0]  # Append the first character to the end

    return string
