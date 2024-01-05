
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



def check(split_words):
    # Check some simple cases
    assert split_words("Hello world!") == ["Hello", "world!"], "Test 1"
    assert split_words("Hello,world!") == ["Hello", "world!"], "Test 2"
    assert split_words("Hello world,!") == ["Hello", "world,!"], "Test 3"
    assert split_words("Hello,Hello,world !") == ["Hello,Hello,world", "!"], "Test 4"
    
    # Check some cases with unique words
    assert split_words("abcdef") == 3, "Test 5"
    assert split_words("aaabb") == 2, "Test 6"
    assert split_words("aaaBb") == 1, "Test 7"
    
    # Check an empty string
    assert split_words("") == 0, "Test 8"

    # Check the function
    check(split_words)
