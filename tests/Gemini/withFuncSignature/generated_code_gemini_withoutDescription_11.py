
from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Performs a bitwise XOR operation on two strings of equal length,
    treating each character's ASCII value as a byte.

    Args:
        a: The first string.
        b: The second string.

    Returns:
        The result of the bitwise XOR operation, as a string.

    Raises:
        ValueError: If the input strings have different lengths.
    """

    if len(a) != len(b):
        raise ValueError("Input strings must have the same length.")

    result_bytes = []
    for i in range(len(a)):
        result_byte = ord(a[i]) ^ ord(b[i])  # XOR the ASCII values of corresponding characters
        result_bytes.append(chr(result_byte))  # Convert back to character

    return "".join(result_bytes)

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(string_xor): 
    assert string_xor('111000', '101010') == '010010' 
    assert string_xor('1', '1') == '0' 
    assert string_xor('0101', '0000') == '0101' 
    
check(string_xor)