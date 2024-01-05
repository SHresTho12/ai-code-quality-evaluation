
def incr_list(l: list):
  """
  Increments each element in a list by 1.

  Args:
      l: A list of numbers.

  Returns:
      A new list with each element incremented by 1.
  """

  # Create a new list to store the incremented values.
  new_list = []

  # Loop through each element in the original list.
  for element in l:
    # Increment the element by 1 and append it to the new list.
    new_list.append(element + 1)

  # Return the new list.
  return new_list

# Example usage:
my_list = [1, 2, 3]
incremented_list = incr_list(my_list)
print(incremented_list)  # Output: [2, 3, 4]
