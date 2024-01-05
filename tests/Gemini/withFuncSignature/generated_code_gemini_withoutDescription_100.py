
def make_a_pile(n):
  """
  This function creates a list of numbers that represents a pile of n stones.

  Args:
    n: The number of stones in the pile.

  Returns:
    A list of numbers representing the pile of stones.

  Examples:
    make_a_pile(3)  # Output: [1, 2, 3]
    make_a_pile(5)  # Output: [1, 2, 3, 2, 1]
  """

  # Initialize an empty list to store the pile
  pile = []

  # Build the pile by adding stones in increasing order, then decreasing
  for i in range(1, n + 1):
    pile.append(i)

  # Remove the last stone to create the final pile shape
  pile.pop()

  return pile

# Example usage
print(make_a_pile(3))  # Output: [1, 2]
print(make_a_pile(5))  # Output: [1, 2, 3, 4]


def check(make_a_pile):
    assert make_a_pile(3) == [3, 5, 7], "Test 3"
    assert make_a_pile(4) == [4, 6, 8, 10], "Test 4"
    assert make_a_pile(5) == [5, 7, 9, 11, 13], "Test 5"
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16], "Test 6"
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22], "Test 8"

# Check some edge cases that are easy to work out by hand.
assert True, "This prints if this assert fails 2 (also good for debugging!)"

check(make_a_pile)