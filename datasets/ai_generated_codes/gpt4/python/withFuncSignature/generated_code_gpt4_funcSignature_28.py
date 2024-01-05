from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate all strings from the list into a single string. """
    return ''.join(strings)

# Example usage
test_strings = ["Hello", " ", "World", "!"]
result = concatenate(test_strings)
result
