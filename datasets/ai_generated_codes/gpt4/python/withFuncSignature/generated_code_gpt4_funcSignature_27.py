def flip_case(string: str) -> str:
    """ Return a new string with flipped case for each character in the input string. """
    return string.swapcase()

# Example usage
test_string = "Hello, World!"
result = flip_case(test_string)
result
