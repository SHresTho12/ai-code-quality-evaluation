
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Generates all possible prefixes of a given string.

    Args:
        string: The input string.

    Returns:
        A list of all prefixes of the string, in order from shortest to longest.
    """

    prefixes = []
    for i in range(len(string) + 1):  # Iterate up to and including the full string
        prefixes.append(string[:i])  # Slice the string from the beginning to each index
    return prefixes
