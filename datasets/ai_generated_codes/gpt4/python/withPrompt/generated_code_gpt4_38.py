def decode_cyclic(s: str) -> str:
    """
    Decode a string encoded with the encode_cyclic function.

    Args:
    s (str): The encoded string.

    Returns:
    str: The decoded string.

    Examples:
    # Test with examples that were encoded using encode_cyclic
    """
    # Split the string into groups of length 3
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group to the right
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

# Example tests
original_str = "abcdefg"
encoded_str = encode_cyclic(original_str)
print(f"Encoded: {encoded_str}")
decoded_str = decode_cyclic(encoded_str)
print(f"Decoded: {decoded_str}")
