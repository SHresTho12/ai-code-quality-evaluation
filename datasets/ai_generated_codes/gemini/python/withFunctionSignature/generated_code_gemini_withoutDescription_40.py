
def triples_sum_to_zero(l: list):
  """
  Finds all triplets in a list that sum to zero.

  Args:
      l: A list of integers.

  Returns:
      A set of all triplets in the list that sum to zero.
  """

  # Use a set to store the found triplets to avoid duplicates.
  triplets = set()

  # Sort the list for efficient two-pointer approach.
  l.sort()

  # Use two pointers (i and j) to iterate through the sorted list.
  i, j = 0, len(l) - 1

  while i < j:
    # Calculate the sum of the current elements.
    current_sum = l[i] + l[j]

    # Check if the sum is equal to zero.
    if current_sum == 0:
      # Add the triplet to the set.
      triplets.add((l[i], l[j], 0))

      # Move both pointers inwards to find other possible triplets.
      i += 1
      j -= 1

    elif current_sum < 0:
      # Move the left pointer inwards to increase the sum.
      i += 1
    else:
      # Move the right pointer inwards to decrease the sum.
      j -= 1

  return triplets

# Example usage
data = [1, -2, 3, -1, 4, 0, 2]
triplets_found = triples_sum_to_zero(data)
print(f"Triplets that sum to zero: {triplets_found}")
