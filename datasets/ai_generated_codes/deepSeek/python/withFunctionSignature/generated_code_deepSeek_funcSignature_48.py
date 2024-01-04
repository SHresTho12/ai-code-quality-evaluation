# This is a generated Python file.
def is_palindrome(text: str):
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum())
    return text == text[::-1]