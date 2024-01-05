def make_palindrome(string: str) -> str:
    # Append the reverse of the string (excluding the first character) to itself
    return string + string[1:][::-1]
