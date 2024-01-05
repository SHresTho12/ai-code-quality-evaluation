
def add(lst):
  """
  Adds all the numbers in a list and returns the sum.

  Args:
    lst: A list of numbers (integers or floats).

  Returns:
    The sum of the numbers in the list.

  Raises:
    TypeError: If the list contains non-numeric elements.
  """

  total = 0
  for item in lst:
    if not isinstance(item, (int, float)):
      raise TypeError("List can only contain numbers.")
    total += item
  return total

# Example usage
numbers = [1, 2, 3, 4, 5]
result = add(numbers)
print(result)  # Output: 15

# Example of error handling
mixed_list = [1, "hello", 3.5]
try:
  add(mixed_list)
except TypeError as e:
  print(e)  # Output: List can only contain numbers.


def check(add):
    # Check some simple cases
    assert add([4, 88]) == 88, "Test 1"
    assert add([4, 5, 6, 7, 2, 122]) == 122, "Test 2"
    assert add([4, 0, 6, 7]) == 0, "Test 3"
    assert add([4, 4, 6, 8]) == 12, "Test 4"

    # Check some edge cases that are easy to work out by hand.

check(add)