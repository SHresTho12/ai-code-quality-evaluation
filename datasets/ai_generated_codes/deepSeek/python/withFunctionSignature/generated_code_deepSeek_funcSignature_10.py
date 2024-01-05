# This is a generated Python file.
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Make a palindrome from given string """
    return string + string[::-1]