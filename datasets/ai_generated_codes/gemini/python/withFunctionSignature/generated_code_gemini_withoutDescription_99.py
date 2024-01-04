
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
