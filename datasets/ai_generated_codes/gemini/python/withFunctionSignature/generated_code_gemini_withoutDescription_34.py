
def unique(l: list):
  """
  Returns a list of unique elements in the input list.

  Args:
      l: A list of elements.

  Returns:
      A new list containing only the unique elements from the input list.
  """
  # Use the built-in set function to remove duplicates and then convert back to a list.
  return list(set(l))

# Example usage
data = [1, 2, 2, 3, 1, 4]
unique_data = unique(data)
print(f"Unique elements: {unique_data}")
