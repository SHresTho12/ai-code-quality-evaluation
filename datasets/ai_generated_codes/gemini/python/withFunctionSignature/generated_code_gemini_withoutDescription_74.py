
def total_match(lst1, lst2):
  """
  This function counts the total number of matching elements between two lists.

  Args:
      lst1: The first list.
      lst2: The second list.

  Returns:
      The total number of elements that appear in both lists.
  """

  count = 0
  for element in lst1:
    if element in lst2:
      count += 1

  return count

# Example usage
lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6, 8]
total_matches = total_match(lst1, lst2)
print(f"Total matching elements: {total_matches}")
