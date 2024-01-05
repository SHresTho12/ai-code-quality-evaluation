
def median(l: list) -> float:
  """
  Calculates the median of a list of numbers.

  Args:
      l: A list of numbers (can be integers or floats).

  Returns:
      The median of the list (float).
  """

  # Sort the list in ascending order
  l.sort()

  # Check if the list has an even or odd number of elements
  if len(l) % 2 == 0:
    # If even, calculate the average of the middle two elements
    return (l[len(l) // 2] + l[(len(l) // 2) - 1]) / 2
  else:
    # If odd, return the middle element
    return l[len(l) // 2]

# Example usage
my_list = [5, 3, 1, 7, 2]
median_value = median(my_list)
print(f"Median of the list: {median_value}")  # Output: Median of the list: 3.5
