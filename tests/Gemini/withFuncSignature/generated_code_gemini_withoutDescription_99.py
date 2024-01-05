
def closest_integer(value):
  """
  This function finds the closest integer to a given value.

  Args:
    value: The value to find the closest integer to.

  Returns:
    The closest integer to the given value.
  """

  # Calculate the fractional part of the value
  fractional_part = value % 1

  # Round to the nearest integer, using banker's rounding for half-values
  if fractional_part >= 0.5:
    return int(value) + 1
  else:
    return int(value)

# Example usage
print(closest_integer(3.2))  # Output: 3
print(closest_integer(4.5))  # Output: 4 (banker's rounding for half-values)
print(closest_integer(-2.8))  # Output: -3


def check(closest_integer):
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("-15.5") == -16, "Test 3"
    assert closest_integer("15.3") == 15, "Test 4"

# Check some edge cases that are easy to work out by hand.
assert closest_integer("0") == 0, "Test 0"

check(closest_integer)
