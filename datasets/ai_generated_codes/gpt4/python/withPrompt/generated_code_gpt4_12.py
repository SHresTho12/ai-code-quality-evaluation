from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """Return the longest string from a list of strings, or None if the list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string, or None if the list is empty.

    Examples:
    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    return max(strings, key=len)
