
def common(l1: list, l2: list) -> list:
  """
  Finds the elements that are common to two lists.

  Args:
      l1: The first list (list).
      l2: The second list (list).

  Returns:
      A list containing the elements that are common to both lists (list).
  """

  # Use set intersection to find common elements
  return list(set(l1) & set(l2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9]
common_elements = common(list1, list2)
print(f"Common elements: {common_elements}")  # Output: Common elements: [3, 5]
