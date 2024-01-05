
def sort_array(array):
  """
  Sorts a 2D array by the sum of its elements in each row, in descending order.

  Args:
    array: A 2D array of numbers.

  Returns:
    A new 2D array with the rows sorted by the sum of their elements.
  """

  # Use the sum of each row as the key for sorting
  sorted_array = sorted(array, key=lambda row: sum(row), reverse=True)

  return sorted_array

# Example usage
array = [[1, 3, 4], [2, 5, 1], [7, 2, 0]]

sorted_array = sort_array(array)

print("Original array:")
for row in array:
  print(row)

print("\nSorted array:")
for row in sorted_array:
  print(row)
