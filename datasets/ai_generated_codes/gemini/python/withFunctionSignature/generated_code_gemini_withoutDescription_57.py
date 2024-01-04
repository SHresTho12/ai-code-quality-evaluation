
def monotonic(l: list) -> bool:
  """
  Checks if a list is monotonically increasing or decreasing.

  Args:
      l: The list to check (list).

  Returns:
      True if the list is monotonically increasing or decreasing, False otherwise (bool).
  """

  if len(l) <= 1:
    return True

  # Check for increasing order
  increasing = all(a <= b for a, b in zip(l[:-1], l[1:]))

  # Check for decreasing order (reverse the list and check for increasing)
  decreasing = all(a <= b for a, b in zip(l[::-1][:-1], l[::-1][1:]))

  return increasing or decreasing

# Example usage
test_cases = [
    ([1, 2, 3, 4, 5], True),  # Increasing
    ([5, 4, 3, 2, 1], True),  # Decreasing
    ([1, 3, 2, 4, 5], False),  # Not monotonic
    ([5, 3, 1, 4, 2], False),  # Not monotonic
]

for l, expected in test_cases:
  result = monotonic(l)
  assert result == expected, f"Expected {l} to be {'monotonically increasing or decreasing' if expected else 'not monotonic'}, got {result}"

print("All test cases passed!")
