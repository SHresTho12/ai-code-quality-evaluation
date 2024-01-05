
def split_words(txt):
  """
  Splits a string into a list of words, removing punctuation and whitespace.

  Args:
      txt: The string to be split.

  Returns:
      A list of words in the string.
  """
  # Use regular expressions to remove punctuation and whitespace.
  import re
  words = re.findall(r"\w+", txt.lower())
  return words

# Example usage
text = "This is a sample text with punctuation! and some whitespace."
words = split_words(text)
print(f"Words: {words}")
