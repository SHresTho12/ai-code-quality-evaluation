
def get_positive(l: list) -> list:
  """
  Returns a new list containing only the positive numbers from the input list.

  Args:
      l: A list of numbers.

  Returns:
      A new list containing only the positive numbers from the input list.

  """

  positive_numbers = [num for num in l if num > 0]
  return positive_numbers

# Example usage
test_list = [-2, 5, 0, -1, 3, 7, -4]
positive_list = get_positive(test_list)
print(f"Original list: {test_list}")
print(f"Positive numbers: {positive_list}")



METADATA = {} 
def check(get_positive): 
    assert get_positive([-1, -2, 4, 5, 6]) == [4, 5, 6] 
    assert get_positive([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1] 
    assert get_positive([-1, -2]) == [] 
    assert get_positive([]) == [] 
    
check(get_positive)