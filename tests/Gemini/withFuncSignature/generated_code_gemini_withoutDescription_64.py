
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


def check(vowels_count):
    # Check some simple cases
    assert vowels_count("abcde") == 2, "Test 1"
    assert vowels_count("Alone") == 3, "Test 2"
    assert vowels_count("key") == 2, "Test 3"
    assert vowels_count("bye") == 1, "Test 4"
    assert vowels_count("keY") == 2, "Test 5"
    assert vowels_count("bYe") == 1, "Test 6"
    assert vowels_count("ACEDY") == 3, "Test 7"
    
    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

check(vowels_count)