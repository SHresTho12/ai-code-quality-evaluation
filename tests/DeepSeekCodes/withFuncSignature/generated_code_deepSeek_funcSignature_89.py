# This is a generated Python file.
def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            result += chr((ord(char) - ascii_offset + 1) % 26 + ascii_offset)
        else:
            result += char
    return result


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
