
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


def check(select_words):
    # Check some simple cases
    assert select_words("Mary had a little lamb", 4) == ["little"], "Test 1"
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"], "Test 2"
    assert select_words("simple white space", 2) == [], "Test 3"
    assert select_words("Hello world", 4) == ["world"], "Test 4"
    assert select_words("Uncle sam", 3) == ["Uncle"], "Test 5"

    # Check some edge cases that are easy to work out by hand.
    assert select_words("", 4) == [], "Test 6"
    assert select_words("a b c d e f", 1) == ["b", "c", "d", "f"], "Test 7"

    # Check the function
    check(select_words)
