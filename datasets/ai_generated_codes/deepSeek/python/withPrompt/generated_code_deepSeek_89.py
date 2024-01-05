def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + 2*2) % 26 + ascii_offset)
        else:
            result += char
    return result