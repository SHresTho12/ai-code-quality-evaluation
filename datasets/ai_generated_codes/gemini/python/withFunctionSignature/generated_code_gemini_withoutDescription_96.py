
def count_up_to(n):
  """
  This function counts up from 1 to a given number, inclusive.

  Args:
    n: The number to count up to.

  Returns:
    A list of numbers from 1 to n.
  """

  count_list = []
  for i in range(1, n + 1):
    count_list.append(i)
  return count_list

# Example usage
print(count_up_to(5))  # Output: [1, 2, 3, 4, 5]
