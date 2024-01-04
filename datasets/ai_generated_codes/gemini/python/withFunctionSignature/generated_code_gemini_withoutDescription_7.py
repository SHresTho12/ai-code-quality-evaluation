
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filters a list of strings, keeping only those that contain a specific substring.

    Args:
        strings: A list of strings to filter.
        substring: The substring to search for within the strings.

    Returns:
        A new list containing only the strings that contain the given substring.
    """

    result = []
    for string in strings:
        if substring in string:
            result.append(string)

    return result
