
def max_element(l: list):
  """
  Finds the maximum element in a list.

  Args:
      l: A list of elements.

  Returns:
      The maximum element in the list, or None if the list is empty.
  """

  if not l:
    return None

  # Initialize the current maximum to the first element.
  max_element = l[0]

  # Loop through the remaining elements and update the maximum if necessary.
  for element in l[1:]:
    if element > max_element:
      max_element = element

  return max_element

# Example usage
data = [1, 2, 3, 4, 5]
max_value = max_element(data)
print(f"Maximum element: {max_value}")


METADATA = {} 
def check(max_element): 
  assert max_element([1, 2, 3]) == 3 
  assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124 
  
check(max_element)