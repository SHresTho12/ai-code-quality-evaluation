
def remove_vowels(text):
  """
  Removes all vowels from a given string.

  Args:
      text: The string to remove vowels from (str).

  Returns:
      A new string with all vowels removed (str).
  """

  vowels = "aeiouAEIOU"
  return "".join([char for char in text if char not in vowels])

# Example usage
text = "This is a string with vowels."
no_vowels_text = remove_vowels(text)
print(f"Original text: {text}")
print(f"Text without vowels: {no_vowels_text}")
