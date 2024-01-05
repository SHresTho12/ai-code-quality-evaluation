
def vowels_count(s):
  """Counts the number of vowels in a string.

  Args:
      s: The string to count vowels in.

  Returns:
      The number of vowels in the string.
  """

  vowels = "aeiouAEIOU"
  count = 0
  for char in s:
    if char in vowels:
      count += 1
  return count

# Test cases
test_cases = [
    ("hello", 2),
    ("world", 1),
    ("apple", 2),
    ("amazing", 3),
    ("bootcamp", 3),
    ("python", 2),
    ("empty", 2),
    ("quiet", 3),
    ("rhythm", 0),
    ("strength", 2),
    ("SCHOOL", 3),
    ("12345", 0),
    ("", 0),
]

for test_case, expected_result in test_cases:
  result = vowels_count(test_case)
  assert result == expected_result, f"Test case '{test_case}' failed: expected {expected_result}, got {result}"

print("All test cases passed!")
