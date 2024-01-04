
def get_row(lst, x):
  """
  Retrieves the row containing the element x in a nested list.

  Args:
    lst: A nested list of elements.
    x: The element to search for.

  Returns:
    The row containing the element x, or None if not found.
  """

  for row in lst:
    if x in row:
      return row
  return None

# Example usage
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target_element = 5

found_row = get_row(nested_list, target_element)

if found_row:
  print(f"Found element {target_element} in row: {found_row}")
else:
  print(f"Element {target_element} not found in the list.")
