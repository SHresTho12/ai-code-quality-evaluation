# This is a generated Python file.
def is_palindrome(text: str):
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum())
    return text == text[::-1]



METADATA = {}

def check(is_palindrome):
    assert is_palindrome('') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('zbcd') == False
    assert is_palindrome('xywyx') == True
    assert is_palindrome('xywyz') == False
    assert is_palindrome('xywzx') == False

check(is_palindrome)
