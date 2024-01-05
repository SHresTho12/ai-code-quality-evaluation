def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    Args:
    n (int): The upper limit of the number sequence.

    Returns:
    str: A space-delimited string of numbers from 0 to n.

    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(i) for i in range(n + 1))
METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(string_sequence): 
    assert string_sequence(0) == '0' 
    assert string_sequence(3) == '0 1 2 3' 
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10' 
    
check(string_sequence)