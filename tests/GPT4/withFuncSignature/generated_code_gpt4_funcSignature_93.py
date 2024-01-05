def encode(message, shift=3):
    """
    Encodes a message by shifting each letter a fixed number of places down the alphabet.

    :param message: The string to be encoded.
    :param shift: The number of characters to shift (default is 3).
    :return: The encoded message.
    """
    encoded_message = []

    for char in message:
        if char.isalpha():  # Check if character is an alphabet
            shift_amount = shift % 26

            if char.islower():
                encoded_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encoded_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))

            encoded_message.append(encoded_char)
        else:
            # Non-alphabetic characters are added as is
            encoded_message.append(char)

    return ''.join(encoded_message)


def check(encode):
    # Check some simple cases
    assert encode('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert encode('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert encode('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert encode('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert encode("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"

check(encode)