
def circular_shift(x, shift):
  """Performs a circular shift on a list or array.

  Args:
      x: The list or array to shift (list or numpy.ndarray).
      shift: The number of positions to shift (positive or negative).

  Returns:
      A new list or array with the elements shifted circularly.
  """

  # Handle negative shifts
  if shift < 0:
    shift = len(x) + shift

  # Handle shifts beyond the list/array length
  shift %= len(x)

  # Create a new list to store the shifted elements
  shifted_x = [None] * len(x)

  # Perform the circular shift
  for i in range(len(x)):
    shifted_x[(i + shift) % len(x)] = x[i]

  return shifted_x

# Example usage
my_list = [1, 2, 3, 4, 5]

# Shift the list by 2 positions to the right
shifted_list = circular_shift(my_list, 2)
print(f"Original list: {my_list}")
print(f"Shifted list (right by 2): {shifted_list}")

# Shift the list by 1 position to the left
shifted_list = circular_shift(my_list, -1)
print(f"Shifted list (left by 1): {shifted_list}")

# Shift a NumPy array
import numpy as np
my_array = np.array([6, 7, 8, 9, 10])
shifted_array = circular_shift(my_array, 3)
print(f"Original array: {my_array}")
print(f"Shifted array: {shifted_array}")
