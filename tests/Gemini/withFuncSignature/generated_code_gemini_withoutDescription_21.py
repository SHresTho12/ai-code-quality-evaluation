
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
  """
  Rescales a list of numbers to the unit interval (0, 1).

  Args:
      numbers: A list of floating-point numbers.

  Returns:
      A new list with the same length as the original, where each element is scaled to the range (0, 1).

  Notes:
      - If all elements in the list are equal, the function returns a list filled with the same value.
      - If the list is empty, the function returns an empty list.

  """

  if not numbers:
    return []

  # Find the minimum and maximum values in the list.
  min_value = min(numbers)
  max_value = max(numbers)

  # Check if all elements are equal.
  if min_value == max_value:
    return [min_value] * len(numbers)

  # Calculate the scaling factor.
  scaling_factor = 1 / (max_value - min_value)

  # Apply the scaling factor to each element.
  scaled_numbers = [scaling_factor * (num - min_value) for num in numbers]

  return scaled_numbers

# Example usage
test_numbers = [1.2, 3.4, 2.1, 5.0, 4.3]
scaled_numbers = rescale_to_unit(test_numbers)
print(f"Rescaled numbers: {scaled_numbers}")

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(rescale_to_unit): 
    assert rescale_to_unit([2.0, 49.9]) == [0.0, 1.0] 
    assert rescale_to_unit([100.0, 49.9]) == [1.0, 0.0] 
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0] 
    assert rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0]) == [0.25, 0.0, 1.0, 0.5, 0.75] 
    assert rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0]) == [0.25, 0.0, 1.0, 0.5, 0.75] 
    
check(rescale_to_unit)