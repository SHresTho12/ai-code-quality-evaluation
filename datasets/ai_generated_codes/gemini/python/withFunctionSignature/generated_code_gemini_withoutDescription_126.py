
def is_sorted(lst):
  """
  Checks if a list is sorted in ascending order.

  Args:
      lst: The list to be checked.

  Returns:
      True if the list is sorted, False otherwise.
  """
  if len(lst) <= 1:
    return True
  for i in range(1, len(lst)):
    if lst[i-1] > lst[i]:
      return False
  return True

# Example usage
test_list1 = [1, 2, 3, 4, 5]
test_list2 = [5, 4, 3, 2, 1]

print(f"List 1 is sorted: {is_sorted(test_list1)}")
print(f"List 2 is sorted: {is_sorted(test_list2)}")
