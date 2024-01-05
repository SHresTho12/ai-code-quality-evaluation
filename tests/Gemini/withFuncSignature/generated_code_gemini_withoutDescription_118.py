
VOWELS = "aeiou"

def get_closest_vowel(word):
  """
  Finds the closest vowel to a given character in a word.

  Args:
    word: A string representing the word.

  Returns:
    A string representing the closest vowel to the character in the word.
  """

  min_distance = float('inf')
  closest_vowel = None
  for char in word:
    if char in VOWELS:
      continue
    for vowel in VOWELS:
      distance = abs(ord(char) - ord(vowel))
      if distance < min_distance:
        min_distance = distance
        closest_vowel = vowel
  return closest_vowel

# Example usage
word = "rhythm"
closest_vowel = get_closest_vowel(word)
print(f"Closest vowel to 'h' in '{word}': {closest_vowel}")  # Output: i


def check(get_closest_vowel):
    # Check some simple cases
    assert get_closest_vowel("yogurt") == "u", "Test 1"
    assert get_closest_vowel("full") == "u", "Test 2"
    assert get_closest_vowel("easy") == "", "Test 3"
    assert get_closest_vowel("eAsy") == "", "Test 4"
    assert get_closest_vowel("ali") == "", "Test 5"
    assert get_closest_vowel("bad") == "a", "Test 6"
    assert get_closest_vowel("most") == "o", "Test 7"
    assert get_closest_vowel("ab") == "", "Test 8"
    assert get_closest_vowel("ba") == "", "Test 9"
    assert get_closest_vowel("quick") == "", "Test 10"
    assert get_closest_vowel("anime") == "i", "Test 11"
    assert get_closest_vowel("Asia") == "", "Test 12"
    assert get_closest_vowel("Above") == "o", "Test 13"

    # Check the function
    check(get_closest_vowel)
