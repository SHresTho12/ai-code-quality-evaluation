
def reverse_delete(s, c):
    """
    Deletes characters in s that are in c, then checks if the remaining string is a palindrome.

    Args:
        s: The original string.
        c: The string containing characters to be deleted.

    Returns:
        A tuple containing:
            - The modified string after character deletions.
            - True if the modified string is a palindrome, False otherwise.
    """

    result = ""
    for char in s:
        if char not in c:
            result += char

    return result, result == result[::-1]  # Check for palindrome
