from typing import List


def concatenate(strings: List[str]) -> str:
    """Concatenate a list of strings into a single string.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    str: A single string formed by concatenating all the strings in the list.

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(concatenate): 
    assert concatenate([]) == '' 
    assert concatenate(['x', 'y', 'z']) == 'xyz' 
    assert concatenate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk' 
    
check(concatenate)