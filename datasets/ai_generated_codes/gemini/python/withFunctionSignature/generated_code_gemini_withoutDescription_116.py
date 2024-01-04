
def sort_array(arr):
  """
  Sorts an array in ascending order using the merge sort algorithm.

  Args:
    arr: A list of numbers.

  Returns:
    A new list with the elements of arr sorted in ascending order.
  """

  def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
      left: A sorted list.
      right: A sorted list.

    Returns:
      A new list containing the elements of left and right in ascending order.
    """

    merged = []
    while left and right:
      if left[0] <= right[0]:
        merged.append(left.pop(0))
      else:
        merged.append(right.pop(0))
    merged.extend(left)
    merged.extend(right)
    return merged

  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left = sort_array(arr[:mid])
  right = sort_array(arr[mid:])
  return merge(left, right)

# Example usage
arr = [5, 2, 1, 3, 4]
sorted_arr = sort_array(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5]
