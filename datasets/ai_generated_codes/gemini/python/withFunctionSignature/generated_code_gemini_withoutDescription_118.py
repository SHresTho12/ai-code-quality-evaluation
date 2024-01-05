
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
