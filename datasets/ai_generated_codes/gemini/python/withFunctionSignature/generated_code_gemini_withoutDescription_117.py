
def select_words(s, n):
  """
  Selects the n longest words from a string.

  Args:
    s: A string.
    n: The number of words to select.

  Returns:
    A list of the n longest words in the string, in descending order of length.
  """

  words = s.split()
  words.sort(key=len, reverse=True)
  return words[:n]

# Example usage
s = "This is a sentence with some long and short words."
n = 3
selected_words = select_words(s, n)
print(selected_words)  # Output: ['sentence', 'words.', 'short']
