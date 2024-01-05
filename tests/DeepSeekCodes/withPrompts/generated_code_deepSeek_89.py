def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + 2*2) % 26 + ascii_offset)
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