def remove_vowels(text):
    """
    Remove vowels from a string.

    Args:
    text (str): The input string.

    Returns:
    str: The string with vowels removed.

    Example:
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = "AEIOUaeiou"
    return ''.join([char for char in text if char not in vowels])

# Example tests
print(remove_vowels('abcdef\nghijklm'))  # Output: 'bcdf\nghjklm'
print(remove_vowels('aaaaa'))  # Output: ''
METADATA = {}

def check(remove_vowels):
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert remove_vowels('fedcba') == 'fdcb'
    assert remove_vowels('eeeee') == ''
    assert remove_vowels('acBAA') == 'cB'
    assert remove_vowels('EcBOO') == 'cB'
    assert remove_vowels('ybcd') == 'ybcd'

check(remove_vowels)