def strlen(string: str) -> int:
    """Return the length of a given string.

    Args:
    string (str): The input string.

    Returns:
    int: The length of the string.

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)
METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(strlen): 
    assert strlen('') == 0 
    assert strlen('x') == 1 
    assert strlen('asdasnakj') == 9 
    
check(strlen)