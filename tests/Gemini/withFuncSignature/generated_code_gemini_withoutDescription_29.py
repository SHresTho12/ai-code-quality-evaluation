
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
  """
  Filters a list of strings based on a given prefix.

  Args:
      strings: A list of strings to filter.
      prefix: The prefix to match against.

  Returns:
      A new list containing only the strings that start with the given prefix.

  Notes:
      - The function uses a list comprehension for efficiency.

  """

  filtered_strings = [string for string in strings if string.startswith(prefix)]
  return filtered_strings

# Example usage
test_strings = ["apple", "banana", "orange", "apricot"]
filtered_fruits = filter_by_prefix(test_strings, "ap")
print(f"Strings starting with 'ap': {filtered_fruits}")


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(filter_by_prefix): 
    assert filter_by_prefix([], 'john') == [] 
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx'] 
    
check(filter_by_prefix)