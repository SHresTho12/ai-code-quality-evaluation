
def sort_third(l: list):
  """
  Sorts a list of lists based on the third element in each sublist.

  Args:
      l: A list of lists.

  Returns:
      A new list with the sublists sorted based on their third element.
  """
  # Use the key parameter of the sorted function to specify the sorting criteria.
  # In this case, we want to sort based on the third element of each sublist.
  return sorted(l, key=lambda x: x[2])

# Example usage
data = [[1, 2, 3], [4, 5, 1], [7, 8, 2]]
sorted_data = sort_third(data)
print(f"Sorted data: {sorted_data}")
