from typing import List

def all_prefixes(string: str) -> List[str]:
    """Return a list of all prefixes of the input string, from shortest to longest.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of all prefixes of the string.

    Examples:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]
