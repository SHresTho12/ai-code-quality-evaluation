def encrypt(s):
    """
    Encrypt the given string by shifting each letter down the alphabet by two multiplied by two places.
    """
    result = []
    for char in s:
        if char.isalpha():
            # Check if the character is alphabetic
            offset = 2 * 2
            if char.islower():
                # For lowercase letters
                new_char = chr(((ord(char) - ord('a') + offset) % 26) + ord('a'))
            else:
                # For uppercase letters
                new_char = chr(((ord(char) - ord('A') + offset) % 26) + ord('A'))
            result.append(new_char)
        else:
            # If not alphabetic, keep the character as is
            result.append(char)
    return ''.join(result)
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