
def count_upper(s):
  """
  This function counts the number of uppercase letters in a string.

  Args:
    s: The string to count uppercase letters in.

  Returns:
    The number of uppercase letters in s.
  """

  count = 0
  for char in s:
    if char.isupper():
      count += 1
  return count

# Example usage
print(count_upper("Hello World"))  # Output: 2


def check(count_upper):
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
    assert count_upper('B') == 0
    assert count_upper('U') == 1
    assert count_upper('') == 0
    assert count_upper('EEEE') == 2

# Check some edge cases that are easy to work out by hand.
assert True

check(count_upper)
