def string_xor(a: str, b: str) -> str:
    """Perform binary XOR on two input strings consisting of 1s and 0s.

    Args:
    a (str): The first binary string.
    b (str): The second binary string.

    Returns:
    str: The result of the binary XOR operation as a string.

    Examples:
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings are of the same length
    max_length = max(len(a), len(b))
    a = a.zfill(max_length)
    b = b.zfill(max_length)

    # Perform XOR operation
    result = ''.join('1' if x != y else '0' for x, y in zip(a, b))
    return result
