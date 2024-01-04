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