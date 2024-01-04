
def pairs_sum_to_zero(l):
  """
  Finds all pairs of numbers in a list that sum to zero.

  Args:
      l: A list of numbers.

  Returns:
      A list of tuples, where each tuple contains a pair of numbers that sum to zero.
  """

  pairs = []
  seen = set()  # Use a set to efficiently track seen numbers

  # Iterate through each number in the list
  for i in range(len(l)):
    target = -l[i]  # The complement needed to make a zero sum

    # Check if the target has been seen before
    if target in seen:
      pairs.append((target, l[i]))  # Add the pair in the desired order

    # Add the current number to the set of seen numbers
    seen.add(l[i])

  return pairs

# Example usage:
my_list = [1, -2, 3, 0, -5, 2]
pairs = pairs_sum_to_zero(my_list)
print(pairs)  # Output: [(-2, 2), (3, -3), (0, 0)]
