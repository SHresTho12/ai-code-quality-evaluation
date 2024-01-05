def encrypt(s, shift=3):
    """
    Encrypts a string using a simple Caesar Cipher method.

    :param s: The string to be encrypted.
    :param shift: The number of characters to shift (default is 3).
    :return: The encrypted string.
    """
    encrypted = []

    for char in s:
        if char.isalpha():  # Check if character is an alphabet
            shift_amount = shift % 26

            if char.islower():
                encrypted.append(chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a')))
            else:
                encrypted.append(chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A')))
        else:
            # Non-alphabetic characters are added as is
            encrypted.append(char)

    return ''.join(encrypted)


def check(encrypt):
    # Check some simple cases
    assert encrypt('hi') == 'lm', "Error"
    assert encrypt('asdfghjkl') == 'ewhjklnop', "Error"
    assert encrypt('gf') == 'kj', "Error"
    assert encrypt('et') == 'ix', "Error"
    assert encrypt('faewfawefaewg') == 'jeiajeaijeiak', "Error"
    assert encrypt('hellomyfriend') == 'lippsqcjvmirh', "Error"
    assert encrypt('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh') == 'hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', "Error"

    # Check some edge cases that are easy to work out by hand.
    assert encrypt('a') == 'e', "Error"

check(encrypt)