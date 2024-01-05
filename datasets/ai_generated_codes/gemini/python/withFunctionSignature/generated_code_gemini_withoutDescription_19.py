
from typing import List

def sort_numbers(numbers: str) -> str:
  """
  Sorts a string containing numbers separated by spaces or commas.

  Args:
      numbers: A string containing numbers separated by spaces or commas.

  Returns:
      A new string with the numbers sorted in ascending order, separated by spaces.

  Notes:
      - The function handles both integer and floating-point numbers.
      - The original string is not modified.
  """

  # Split the string into a list of numbers.
  number_list = [float(num) for num in numbers.split() if num]

  # Sort the list of numbers.
  sorted_numbers = sorted(number_list)

  # Convert the sorted list back to a string with spaces.
  sorted_string = " ".join(str(num) for num in sorted_numbers)

  return sorted_string

# Example usage
test_string = "1.2 3 5.4 2.1"
sorted_string = sort_numbers(test_string)
print(f"Sorted numbers: {sorted_string}")
