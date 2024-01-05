
def count_nums(arr):
  """
  This function counts the number of occurrences of each element in an array.

  Args:
      arr: A list of numbers.

  Returns:
      A dictionary where the keys are the numbers in the array and the values are the
      number of times each number appears.
  """

  counts = {}
  for num in arr:
    if num in counts:
      counts[num] += 1
    else:
      counts[num] = 1
  return counts
