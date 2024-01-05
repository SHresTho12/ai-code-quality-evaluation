from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter a list of strings, keeping only those that start with a specified prefix.

    Args:
    strings (List[str]): A list of strings.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: A list of strings that start with the specified prefix.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(filter_by_prefix): 
    assert filter_by_prefix([], 'john') == [] 
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx'] 
    
check(filter_by_prefix)