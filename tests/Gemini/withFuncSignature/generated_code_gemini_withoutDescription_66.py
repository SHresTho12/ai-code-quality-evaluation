
def digitSum(s):
  """
  Calculates the sum of digits present in a string.

  Args:
      s: The input string that may contain digits.

  Returns:
      The sum of all digits in the string.
  """

  sum_of_digits = 0

  for char in s:
    if char.isdigit():
      sum_of_digits += int(char)  # Convert the digit character to an integer and add it to the sum

  return sum_of_digits

# Example usage
test_cases = [
    ("abc123xyz", 6),
    ("hello world 42", 6),
    ("no digits here", 0),
    ("123", 6),
    ("1a2b3c", 6),
    ("", 0),
]

for test_case, expected_result in test_cases:
  result = digitSum(test_case)
  assert result == expected_result, f"Test case '{test_case}' failed: expected {expected_result}, got {result}"

print("All test cases passed!")


def check(digitSum):
    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert digitSum("") == 0, "Error"
    assert digitSum("abAB") == 131, "Error"
    assert digitSum("abcCd") == 67, "Error"
    assert digitSum("helloE") == 69, "Error"
    assert digitSum("woArBld") == 131, "Error"
    assert digitSum("aAaaaXa") == 153, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert digitSum(" How are yOu?") == 151, "Error"
    assert digitSum("You arE Very Smart") == 327, "Error"

check(digitSum)