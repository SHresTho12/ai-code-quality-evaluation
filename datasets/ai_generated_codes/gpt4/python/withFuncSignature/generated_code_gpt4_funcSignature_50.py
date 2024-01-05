def decode_shift(s: str):
    """
    Decodes a string that was encoded by shifting every character by 5 in the alphabet.
    Assumes the input string is lowercase and alphabetic.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
