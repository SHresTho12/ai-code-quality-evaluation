
def decode_shift(s: str) -> str:
    """
    returns decoded string by shifting every character by -5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

# Example usage
encoded_string = encode_shift("hello world")
print(encoded_string)  # Output: mjqqt btwqi

decoded_string = decode_shift(encoded_string)
print(decoded_string)  # Output: hello world
