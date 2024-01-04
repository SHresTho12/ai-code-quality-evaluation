
def pluck(arr):
  """
  Plucks the second element from each nested list in a given array.

  Args:
      arr: The input array containing nested lists.

  Returns:
      A new array containing the second element from each nested list.
  """

  plucked_values = []
  for sublist in arr:
    if len(sublist) >= 2:
      plucked_values.append(sublist[1])  # Access the second element (index 1)
    else:
      plucked_values.append(None)  # Handle cases where sublists have fewer than 2 elements

  return plucked_values

# Example usage
array = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
result = pluck(array)
print(result)  # Output: [2, 5, None, 8]
