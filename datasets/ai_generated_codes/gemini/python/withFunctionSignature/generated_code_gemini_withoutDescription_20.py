
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
  """
  Finds the two closest elements in a list of numbers.

  Args:
      numbers: A list of floating-point numbers.

  Returns:
      A tuple containing the two closest elements in the list.

  Notes:
      - If the list has less than two elements, the function returns None.
      - If there are multiple pairs of equally close elements, the first pair encountered is returned.

  """

  if len(numbers) < 2:
    return None

  # Initialize variables to track the closest elements and their difference.
  closest_element1 = numbers[0]
  closest_element2 = numbers[1]
  smallest_difference = abs(closest_element2 - closest_element1)

  # Loop through the remaining elements, checking for closer pairs.
  for i in range(2, len(numbers)):
    current_element = numbers[i]
    difference1 = abs(current_element - closest_element1)
    difference2 = abs(current_element - closest_element2)

    # Update the closest elements if a closer pair is found.
    if difference1 < smallest_difference:
      smallest_difference = difference1
      closest_element2 = closest_element1
      closest_element1 = current_element
    elif difference2 < smallest_difference:
      smallest_difference = difference2
      closest_element2 = current_element

  return closest_element1, closest_element2

# Example usage
test_numbers = [1.2, 3.4, 2.1, 5.0, 4.3]
closest_pair = find_closest_elements(test_numbers)
print(f"Closest elements: {closest_pair[0]} and {closest_pair[1]}")
