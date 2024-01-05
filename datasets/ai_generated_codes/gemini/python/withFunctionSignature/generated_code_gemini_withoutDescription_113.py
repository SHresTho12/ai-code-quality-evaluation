
def odd_count(lst):
  """Counts the number of odd numbers in a list.

  Args:
    lst: A list of numbers.

  Returns:
    The number of odd numbers in the list.
  """

  count = 0
  for num in lst:
    if num % 2 != 0:  # Check if the number is odd
      count += 1
  return count
