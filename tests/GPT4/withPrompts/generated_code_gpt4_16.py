def count_distinct_characters(string: str) -> int:
    """Count the number of distinct characters in a string, case-insensitive.

    Args:
    string (str): The input string.

    Returns:
    int: The number of distinct characters in the string.

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string.lower()))

METADATA = { 'author': 'jt', 'dataset': 'test' } 

def check(count_distinct_characters): 
    assert count_distinct_characters('') == 0 
    assert count_distinct_characters('abcde') == 5 
    assert count_distinct_characters('abcde' + 'cade' + 'CADE') == 5 
    assert count_distinct_characters('aaaaAAAAaaaa') == 1 
    assert count_distinct_characters('Jerry jERRY JeRRRY') == 5 
    
check(count_distinct_characters)