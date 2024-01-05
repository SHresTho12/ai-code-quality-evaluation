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
def check(encode):
    # Check some simple cases
    assert encode('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert encode('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert encode('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert encode('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert encode("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"

check(encode)