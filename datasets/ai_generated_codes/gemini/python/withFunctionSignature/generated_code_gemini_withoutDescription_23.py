
def strlen(string: str) -> int:
  """
  Calculates the length of a string.

  Args:
      string: The string whose length is to be determined.

  Returns:
      An integer representing the length of the string.

  Notes:
      - The function uses the built-in `len` function for efficiency.

  """

  return len(string)

# Example usage
test_string = "Hello, world!"
string_length = strlen(test_string)
print(f"The string '{test_string}' has {string_length} characters.")
