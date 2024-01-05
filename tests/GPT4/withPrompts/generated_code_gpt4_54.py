def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.

    Args:
    s0 (str): The first word.
    s1 (str): The second word.

    Returns:
    bool: True if both words have the same characters, False otherwise.

    Examples:
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # Sort both strings and compare them
    return sorted(s0) == sorted(s1)

# Example tests
print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # Output: True
print(same_chars('abcd', 'dddddddabc'))  # Output: True
print(same_chars('dddddddabc', 'abcd'))  # Output: True
print(same_chars('eabcd', 'dddddddabc'))  # Output: False
print(same_chars('abcd', 'dddddddabce'))  # Output: False
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))  # Output: False
METADATA = {}

def check(same_chars):
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert same_chars('abcd', 'dddddddabc') == True
    assert same_chars('dddddddabc', 'abcd') == True
    assert same_chars('eabcd', 'dddddddabc') == False
    assert same_chars('abcd', 'dddddddabcf') == False
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False
    assert same_chars('aabb', 'aaccc') == False

check(same_chars)