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
