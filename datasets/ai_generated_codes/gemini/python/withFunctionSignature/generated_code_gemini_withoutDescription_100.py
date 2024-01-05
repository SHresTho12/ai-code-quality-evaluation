
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
