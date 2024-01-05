
def decode_cyclic(s: str):
    """
    returns decoded string by reversing cyclic groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

# Example usage
encoded_string = encode_cyclic("ABCDE")
decoded_string = decode_cyclic(encoded_string)

print(f"Encoded string: {encoded_string}")  # Output: BCADE
print(f"Decoded string: {decoded_string}")  # Output: ABCDE


METADATA = {}

def check(decode_cyclic):
    import string
    from random import choice, randint

    letters = string.ascii_lowercase

    for _ in range(100):
        random_str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = decode_cyclic(random_str)
        assert decode_cyclic(encoded_str) == random_str

check(decode_cyclic)