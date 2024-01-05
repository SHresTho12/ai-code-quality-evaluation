
def sort_even(l: list):
  """
  Sorts a list of integers, placing all even numbers before odd numbers while preserving the original order of even and odd numbers among themselves.

  Args:
      l: A list of integers.

  Returns:
      A new list with the even numbers sorted before the odd numbers.
  """

  # Use two separate lists to store even and odd numbers.
  even_numbers = []
  odd_numbers = []

  # Separate the even and odd numbers into their respective lists.
  for number in l:
    if number % 2 == 0:
      even_numbers.append(number)
    else:
      odd_numbers.append(number)

  # Sort the even and odd numbers separately.
  even_numbers.sort()
  odd_numbers.sort()

  # Combine the sorted even and odd numbers back into a single list.
  sorted_list = even_numbers + odd_numbers

  return sorted_list

# Example usage
data = [1, 4, 2, 7, 5, 8, 3, 6]
sorted_data = sort_even(data)
print(f"Sorted list: {sorted_data}")


METADATA = {} 
def check(sort_even): 
    assert tuple(sort_even([1, 2, 3])) == tuple([1, 2, 3]) 
    assert tuple(sort_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123]) 
    assert tuple(sort_even([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10]) 
    
check(sort_even)