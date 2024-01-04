
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
