
def is_palindrome(text: str) -> bool:
  """
  Checks if a given text is a palindrome (reads the same backward and forward).

  Args:
      text: The text to check (str).

  Returns:
      True if the text is a palindrome, False otherwise (bool).
  """

  # Convert the text to lowercase and remove non-alphanumeric characters
  clean_text = "".join(char.lower() for char in text if char.isalnum())

  # Check if the reversed clean text is equal to the original clean text
  return clean_text == clean_text[::-1]

# Example usage
test_cases = [
    ("racecar", True),
    ("madam", True),
    ("level", True),
    ("noon", True),
    ("hannah", True),
    ("hello", False),
    ("world", False),
    ("palindrome", False),
]

for text, expected in test_cases:
  result = is_palindrome(text)
  assert result == expected, f"Expected {text} to be {'a' if expected else 'not'} palindrome, got {result}"

print("All test cases passed!")


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
