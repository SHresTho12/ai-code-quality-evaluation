def encode_shift(s: str):
    """
    Encode a string by shifting every character by 5 positions in the alphabet.

    Args:
    s (str): The input string.

    Returns:
    str: The encoded string.

    Example:
    >>> encode_shift('abc')
    'fgh'
    >>> encode_shift('xyz')
    'cde'
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decode an encoded string by shifting every character back by 5 positions in the alphabet.

    Args:
    s (str): The encoded string.

    Returns:
    str: The decoded string.

    Example:
    >>> decode_shift('fgh')
    'abc'
    >>> decode_shift('cde')
    'xyz'
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

# Example tests
print(encode_shift('abc'))  # Output: 'fgh'
print(decode_shift('fgh'))  # Output: 'abc'
