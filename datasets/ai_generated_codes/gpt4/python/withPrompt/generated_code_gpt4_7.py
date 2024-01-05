from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter a list of strings, keeping only those that contain a specified substring.

    Args:
    strings (List[str]): A list of strings.
    substring (str): The substring to filter by.

    Returns:
    List[str]: A list of strings that contain the specified substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]
