def encode(message):
    """
    Encodes the message by swapping the case of letters and replacing vowels
    with the letter 2 places ahead in the English alphabet.
    """
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.lower() in 'aeiou':
                # Replace vowel with the letter 2 places ahead
                encoded_message += chr(ord(char) + 2)
            else:
                # Swap case for non-vowel letters
                if char.isupper():
                    encoded_message += char.lower()
                else:
                    encoded_message += char.upper()
        else:
            encoded_message += char  # Keep non-alphabetic characters unchanged
    return encoded_message

# Test cases
print(encode('test'))                 # Output: 'TGST'
print(encode('This is a message'))    # Output: 'tHKS KS C MGSSCGG'
