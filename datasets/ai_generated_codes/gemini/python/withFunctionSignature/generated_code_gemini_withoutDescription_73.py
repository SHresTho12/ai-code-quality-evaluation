
def smallest_change(arr):
  """
  This function finds the smallest absolute difference between consecutive elements in a list.

  Args:
      arr: A list of numbers.

  Returns:
      The smallest absolute difference between consecutive elements in the list.

  Raises:
      ValueError: If the list is empty or contains only one element.
  """

  if len(arr) < 2:
    raise ValueError("List must contain at least two elements")

  smallest_diff = abs(arr[1] - arr[0])
  for i in range(1, len(arr) - 1):
    current_diff = abs(arr[i + 1] - arr[i])
    if current_diff < smallest_diff:
      smallest_diff = current_diff

  return smallest_diff

# Example usage
arr = [5, 1, 7, 3, 2]
smallest_diff = smallest_change(arr)
print(f"Smallest absolute difference: {smallest_diff}")
