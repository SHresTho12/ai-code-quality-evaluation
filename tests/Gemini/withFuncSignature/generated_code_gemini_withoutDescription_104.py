
def unique_digits(x):
  """
  This function returns a set of the unique digits in a non-negative integer.

  Args:
      x: A non-negative integer.

  Returns:
      A set containing the unique digits in x.
  """

  # Convert the integer to a string of digits.
  digits_str = str(x)

  # Create a set to store the unique digits.
  unique_digits = set()

  # Iterate through each digit in the string.
  for digit in digits_str:
    # Add the digit to the set if it is not already present.
    if digit not in unique_digits:
      unique_digits.add(digit)

  return unique_digits

# Example usage
print(unique_digits(12345))  # Output: {'1', '2', '3', '4', '5'}
print(unique_digits(11111))  # Output: {'1'}
print(unique_digits(0))  # Output: {'0'}


def check(unique_digits):
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33], "Test 1"
    assert unique_digits([152, 323, 1422, 10]) == [], "Test 2"
    assert unique_digits([12345, 2033, 111, 151]) == [111, 151], "Test 3"
    assert unique_digits([135, 103, 31]) == [31, 135], "Test 4"

# Check some edge cases that are easy to work out by hand.
assert True, "This prints if this assert fails (also good for debugging!)"

check(unique_digits)
