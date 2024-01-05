
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
  """
  Removes duplicate elements from a list of integers, preserving the order.

  Args:
      numbers: A list of integers.

  Returns:
      A new list containing the unique elements from the original list, in the same order.

  Notes:
      - The function uses a set to efficiently store and check for duplicates.

  """

  # Create an empty set to store unique elements.
  unique_elements = set()

  # Iterate through the list and add unique elements to the set.
  unique_list = []
  for number in numbers:
    if number not in unique_elements:
      unique_elements.add(number)
      unique_list.append(number)

  # Return the list of unique elements.
  return unique_list

# Example usage
test_list = [1, 2, 3, 1, 4, 2, 5]
unique_list = remove_duplicates(test_list)
print(f"Original list: {test_list}")
print(f"List without duplicates: {unique_list}")


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(remove_duplicates): 
    assert remove_duplicates([]) == [] 
    assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4] 
    assert remove_duplicates([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5] 
    
check(remove_duplicates)