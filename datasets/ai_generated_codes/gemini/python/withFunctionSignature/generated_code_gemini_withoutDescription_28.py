
from typing import List

def concatenate(strings: List[str]) -> str:
  """
  Concatenates a list of strings into a single string.

  Args:
      strings: A list of strings to be joined.

  Returns:
      A new string formed by joining all the elements of the list with an empty separator.

  Notes:
      - The function uses the built-in `join` method for efficiency.

  """

  return "".join(strings)
