
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
  """
  Filters a list of values, keeping only the integers.

  Args:
      values: A list of any type of values.

  Returns:
      A new list containing only the integer elements from the original list.

  Notes:
      - The order of the elements is preserved.
      - Non-integer elements are silently discarded.

  """

  filtered_values = []
  for value in values:
    if isinstance(value, int):
      filtered_values.append(value)

  return filtered_values
