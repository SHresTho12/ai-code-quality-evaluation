def decode_cyclic(s: str):
    """
    Decodes a string encoded by encode_cyclic by cycling groups of three characters to the left.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group to the left. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

# Example usage
encoded_str = encode_cyclic("Hello World!")
decoded_str = decode_cyclic(encoded_str)
print("Encoded:", encoded_str)  # Output: "elHlo olWr!d"
print("Decoded:", decoded_str)  # Output: "Hello World!"

METADATA = {}


def check(decode_cyclic):
    import string
    from random import choice, randint

    letters = string.ascii_lowercase

    for _ in range(100):
        random_str = ''.join(choice(letters) for _ in range(randint(10, 20)))
        encoded_str = decode_cyclic(random_str)
        assert decode_cyclic(encoded_str) == random_str


check(decode_cyclic)
