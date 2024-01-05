from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Return a list of strings from the input list that start with the given prefix. """
    return [s for s in strings if s.startswith(prefix)]

# Example usage
test_strings = ["apple", "banana", "apricot", "cherry", "blueberry"]
test_prefix = "ap"
result = filter_by_prefix(test_strings, test_prefix)
result
